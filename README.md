🧠 LSTM Sentence Prediction Web App

This project is a Deep Learning-based Sentence Prediction System built using an LSTM (Long Short-Term Memory) model and deployed with Streamlit for an interactive web interface.

---

🚀 Features

- Predicts the next word or sentence based on user input
- Uses LSTM neural network for sequence modeling
- Clean and simple Streamlit web app interface
- Fast and interactive predictions

---

🛠️ Technologies Used

- Python 🐍
- TensorFlow / Keras
- LSTM (Deep Learning)
- Streamlit
- NumPy & Pandas

---

📁 Project Structure

📦 lstm-sentence-prediction-app
 ┣ 📜 app.py
 ┣ 📜 model.h5
 ┣ 📜 tokenizer.pkl
 ┣ 📜 notebook.ipynb
 ┣ 📜 requirements.txt
 ┗ 📜 README.md

---

⚙️ How It Works

1. Text data is preprocessed and tokenized
2. Sequences are created for training
3. LSTM model is trained on sequence data
4. Model predicts the next word based on input text
5. Streamlit app takes user input and shows prediction

---

▶️ How to Run the Project

1️⃣ Install dependencies

pip install -r requirements.txt

2️⃣ Run Streamlit app

streamlit run app.py

---

💡 Example

Input:

«"Machine learning is"»

Output:

«"Machine learning is powerful"»

---

📌 Future Improvements

- Use Transformer models (like GPT)
- Improve accuracy with larger dataset
- Add multiple sentence prediction
- Deploy online (Streamlit Cloud / Render)

---

👨‍💻 Author

Krish patel

---

📖 Conclusion

This project demonstrates how LSTM can be used for Natural Language Processing tasks like sentence prediction and how it can be deployed using Streamlit for real-world applications.
