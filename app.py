import streamlit as st
import joblib

import pandas as pd
import string
import nltk
nltk.data.path.append("nltk_data")
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps = PorterStemmer()


tfidf = joblib.load("vectorizerFF.pkl")
model = joblib.load("modelFX.pkl")

st.title('Spam Classifier')
input_msg=st.text_area("Enter the message to classify")

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


if st.button('Predict'):
    # 1.preprocess
    transformed_msg2 = transform_text(input_msg)
    # 2.Vectorize
    vector_input = tfidf.transform([transformed_msg2])
    print("Is vectorizer fitted?", hasattr(tfidf, "idf_"))

    # 3.Predict
    result = model.predict(vector_input)
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
    # 4.Display


