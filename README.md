# pySKTranslator

## Inštalácia

```
git clone --depth=1 https://github.com/zdposter/pySKTranslator.git
cd pySKTranslator
wget -P models/en_sk https://huggingface.co/Helsinki-NLP/opus-mt-en-sk/blob/main/pytorch_model.bin
wget -P models/en_sk https://huggingface.co/Helsinki-NLP/opus-mt-en-sk/blob/main/vocab.json
wget -P models/en_sk https://huggingface.co/Helsinki-NLP/opus-mt-en-sk/blob/main/target.spm
wget -P models/en_sk https://huggingface.co/Helsinki-NLP/opus-mt-en-sk/blob/main/source.spm
wget -P models/en_sk https://huggingface.co/Helsinki-NLP/opus-mt-en-sk/blob/main/generation_config.json
wget -P models/en_sk https://huggingface.co/Helsinki-NLP/opus-mt-en-sk/blob/main/config.json

python -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Spustenie

```
python app.py
```

a v prehliadači: http://127.0.0.1:8888
