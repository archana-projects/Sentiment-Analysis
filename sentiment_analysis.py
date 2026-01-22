import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required data (only first time)
nltk.download('vader_lexicon')

# Load dataset
data = pd.read_csv("reviews.csv")

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to get sentiment
def get_sentiment(text):
    score = sia.polarity_scores(text)['compound']
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
data["Sentiment"] = data["Review"].apply(get_sentiment)

# Show results
print(data)

