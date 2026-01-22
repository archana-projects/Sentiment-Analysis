import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download lexicon (first time only)
nltk.download('vader_lexicon')

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

# Page config
st.set_page_config(page_title="Sentiment Analysis")

# Title
st.title("💬 Sentiment Analysis Dashboard")
st.write("Enter a review or sentence to analyze sentiment")

# Text input
user_text = st.text_area("Enter text here:")

# Button
if st.button("Analyze Sentiment"):
    if user_text.strip() == "":
        st.warning("Please enter some text")
    else:
        score = sia.polarity_scores(user_text)["compound"]

        if score >= 0.05:
            st.success("Sentiment: Positive 😊")
        elif score <= -0.05:
            st.error("Sentiment: Negative 😞")
        else:
            st.info("Sentiment: Neutral 😐")

