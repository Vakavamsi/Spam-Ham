import re
import nltk
import streamlit as st
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

@st.cache_resource
def download_nltk_resources():
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)

download_nltk_resources()

def clean(text):
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower()

    tokens = nltk.word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if w not in stop_words]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(w) for w in tokens]

    return " ".join(tokens)

