import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load artifacts
@st.cache_resource
def load_artifacts():
    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)

    with open("max_len.pkl", "rb") as f:
        max_len = pickle.load(f)

    model = load_model("lstm_model.h5")

    return tokenizer, max_len, model

tokenizer, max_len, model = load_artifacts()

# UI
st.title("🔮 Next Word Prediction (LSTM)")
st.write("Type a sentence and predict the next word using your trained LSTM model.")

input_text = st.text_input("Enter your text:", "")

num_words = st.slider("Number of predictions:", 1, 5, 1)

def predict_next_words(text, num_words):
    result = []

    for _ in range(num_words):
        token_list = tokenizer.texts_to_sequences([text])[0]
        token_list = pad_sequences([token_list], maxlen=max_len-1, padding='pre')

        predicted_probs = model.predict(token_list, verbose=0)
        predicted_index = np.argmax(predicted_probs, axis=-1)[0]

        # Convert index to word
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted_index:
                output_word = word
                break

        text += " " + output_word
        result.append(output_word)

    return result, text

if st.button("Predict"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        words, full_text = predict_next_words(input_text, num_words)

        st.subheader("Predicted Words:")
        st.write(" ".join(words))

        st.subheader("Generated Sequence:")
        st.success(full_text)