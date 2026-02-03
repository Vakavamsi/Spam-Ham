import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

def clean(text):
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower()

    # SIMPLE TOKENIZATION (DEPLOYMENT SAFE)
    tokens = text.split()

    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if w not in stop_words]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(w) for w in tokens]

    return " ".join(tokens)


