import numpy as np # linear algebra
import pandas as pd 
import os
import seaborn as sns
from keras.models import load_model

import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.layers import Dropout
import pickle

#loading tokenizer
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)
# Define preprocessing
def preprocess(text):
  if isinstance(text, str):
        text = [text]
  sequences = tokenizer.texts_to_sequences(text)
  padded_sequences = pad_sequences(sequences, maxlen = 10)
  return padded_sequences

# loading model
model = tf.keras.models.load_model("model2.keras")

# Save the entire workflow
def predictions(input_text):
    preprocessed_text = preprocess(input_text)
    prediction = model.predict(preprocessed_text)
    return prediction


def classify(probability):
    threshold = 0.5  # You can adjust this threshold if needed
    if probability >= threshold:
        return "Human generated text"
    else:
        return "LLM generated text"