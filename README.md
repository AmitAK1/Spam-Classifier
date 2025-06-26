# 📩 Spam Classifier Web App

This is a simple **Streamlit-based web application** that classifies whether a given message is **Spam** or **Not Spam** using a trained machine learning model and TF-IDF vectorizer.

---
🌐 Live Demo
You can try the app live here:
👉 https://spam-classifier-7yhtasfpcnkqfz3amyhxv4.streamlit.app/

## 🚀 Features

- Text input for message classification  
- NLP preprocessing (lowercasing, tokenization, stopword removal, stemming)  
- TF-IDF-based vectorization  
- Spam detection using a trained model  
- Real-time prediction output in the browser  

---

## 🧠 Tech Stack

- **Frontend**: Streamlit  
- **ML Model**: Pickled model (`model.pkl`) and TF-IDF vectorizer (`vectorizer.pkl`)  
- **NLP**: NLTK (for stopwords, stemming, tokenization)  
- **Libraries**: scikit-learn, pandas, nltk, pickle, string  

---

## 📁 Files

| File             | Purpose                              |
|------------------|--------------------------------------|
| `app.py`         | Streamlit web app code               |
| `model.pkl`      | Trained ML classification model      |
| `vectorizer.pkl` | TF-IDF vectorizer used for input     |
| `requirements.txt` | Python dependencies               |

---

## ⚙️ Setup Instructions

1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/spam-classifier-app.git
    cd spam-classifier-app
    ```

2. **Create a virtual environment** (optional but recommended)
    ```bash
    python -m venv venv
    # For Linux/macOS
    source venv/bin/activate  
    # For Windows
    venv\Scripts\activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**
    ```bash
    streamlit run app.py
    ```

---

## 🧪 Sample Input

> "Congratulations! You've won a ₹10,00,000 cash prize in the Coca Cola 2025 lucky draw. Send your full name, address & phone number to claim now!"

>"Your account is suspended due to suspicious activity. Click here to verify immediately and avoid permanent closure: http://secure-verify-update.info"

>"Limited Time Offer! Get a FREE iPhone 15 by completing a short survey. Hurry, only 3 left! Claim now: http://win-iphone15-today.net"

>"Dear user, your mobile number has been selected for a ₹5,00,000 lottery by WhatsApp Foundation. Contact Mr. Ramesh at +91-XXXXXXXXXX to receive your amount."

### ✅ Output
> Spam

---

## 📦 Requirements

You can generate the full list using:

pip freeze > requirements.txt
