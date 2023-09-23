#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Form, Request, status
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from langchain.text_splitter import CharacterTextSplitter

from model import Model

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory='templates/')

app = FastAPI()
favicon_path = 'favicon.ico'


@app.on_event('startup')
async def startup_event():
    """
    Initialize translation model.
    """
    start = datetime.datetime.now()
    global TToIT
    model = Model()
    TToIT = model.get_pipeline()
    elapsed = datetime.datetime.now() - start
    print(f'Models loaded after ({elapsed})!')


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    """
    Show favicon
    """
    return FileResponse(favicon_path)


@app.get('/', status_code=200)
async def home(req: Request, result: str = ''):
    """
    Show the main page.
    """
    return TEMPLATES.TemplateResponse(
        'base.html', context={'request': req, 'result': result}
    )


@app.post('/translate')
def translate(req: Request, eng_text: str = Form(None)):
    """
    Translate retrieved text to Slovak.
    """
    url = app.url_path_for('home')
    if not eng_text:
        return TEMPLATES.TemplateResponse(
            'base.html',
            context={'request': req, 'warning': 'Nebol zadaný žiadny text!'},
        )
    text_splitter = CharacterTextSplitter(
        separator='\n\n',
        chunk_size=300,
        chunk_overlap=0,
        length_function=len,
    )
    texts = text_splitter.create_documents([eng_text])
    final_text = ''
    for item in texts:
        line = TToIT(item.page_content)[0]['translation_text']
        final_text += line + '\n'
    return TEMPLATES.TemplateResponse(
        'base.html',
        context={'request': req, 'result': final_text, 'eng_text': eng_text},
    )


if __name__ == '__main__':
    uvicorn.run('app:app', port=8888, reload=True)
