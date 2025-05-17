import torch
import numpy as np
import torch.nn as nn
from torch.utils.data import DataLoader
from utils import *
from transformers import BartTokenizer, BartForConditionalGeneration
import json


with open('data_manipulation\main_training_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')



def generate_summary(text):
    lens_text = len(text)
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=(lens_text//2), min_length=(lens_text//6), length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

article = data["1"]
summary = generate_summary(article)
print(article)
print('\n')
print(summary)

