# -*- coding: utf-8 -*-

import torch
from langchain.text_splitter import CharacterTextSplitter
from transformers import (AutoModelForSeq2SeqLM,
                          AutoModelForSequenceClassification, AutoTokenizer,
                          TFAutoModelForSequenceClassification, pipeline)

Model_ENSK = 'models/en_sk'


class Model:
    """A model class to lead the model and tokenizer"""

    def __init__(self) -> None:
        pass

    def load_model(self):
        """
        Load model
        """
        model = AutoModelForSeq2SeqLM.from_pretrained(Model_ENSK)
        return model

    def load_tokenizer(self):
        """
        Load Tokenizer
        """
        tokenizer = AutoTokenizer.from_pretrained(
            Model_ENSK,
            from_tf=True,
            use_fast=True,
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
        )
        return tokenizer

    def get_pipeline(self):
        """
        Return translator pipeline
        """
        model_tt0it = self.load_model()
        tokenizer_tt0it = self.load_tokenizer()
        TToIT = pipeline(
            'translation', model=model_tt0it, tokenizer=tokenizer_tt0it
        )
        return TToIT
