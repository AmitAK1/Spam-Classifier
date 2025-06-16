📩 Spam Classifier Web App
This is a simple Streamlit-based web application that classifies whether a given message is Spam or Not Spam using a trained machine learning model and TF-IDF vectorizer.

🚀 Features
Text input for message classification

NLP preprocessing (lowercasing, tokenization, stopword removal, stemming)

TF-IDF-based vectorization

Spam detection using a trained model

Real-time prediction output in the browser

🧠 Tech Stack
Frontend: Streamlit

ML Model: Pickled model (model.pkl) and TF-IDF vectorizer (vectorizer.pkl)

NLP: NLTK (for stopwords, stemming, tokenization)

Libraries: scikit-learn, pandas, nltk, pickle, string

📁 Files
File	Purpose
app.py	Streamlit web app code
model.pkl	Trained ML classification model
vectorizer.pkl	TF-IDF vectorizer used for input
requirements.txt	Python dependencies

⚙️ Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/spam-classifier-app.git
cd spam-classifier-app
2. Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the app
bash
Copy
Edit
streamlit run app.py
🧪 Sample Input
vbnet
Copy
Edit
Congratulations! You've won a free vacation to the Bahamas. Call now to claim.
✅ Output
nginx
Copy
Edit
Spam
📦 Requirements
You can generate this using:

bash
Copy
Edit
pip freeze > requirements.txt
But the essentials would be:

txt
Copy
Edit
streamlit
scikit-learn
nltk
pandas
📌 Notes
Make sure you download NLTK stopwords before running the app:

python
Copy
Edit
import nltk
nltk.download('punkt')
nltk.download('stopwords')
The model.pkl and vectorizer.pkl must be present in the same directory.
