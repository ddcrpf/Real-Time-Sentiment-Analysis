import streamlit as st  # for creating a web app to display the final result
import nltk  # natural language toolkit for NLP
from nltk.sentiment.vader import SentimentIntensityAnalyzer  # using SentimentIntensityAnalyzer() class provided by

# the NLTK library

nltk.download('vader_lexicon')  # Valence Aware Dictionary for Sentiment Reasoning, a nltk module that provides
# sentiment scores based on the words used

# using st.write() to display the project title, adding css styling attributes to change the appearance of title
title = '<p style="font-family:sans-serif; font-weight:bold; font-size: 42px; text-align: center;">Real Time ' \
        'Sentiment Analysis</p>'
st.write(title, unsafe_allow_html=True)

# using st.write() to display the project title1 i.e msg asking for user input, adding css styling attributes to
# change the appearance of title
title1 = '<p style="font-family:sans-serif; font-weight:bold; font-size: 20px; margin: 0px;">Enter a Sentence:</p>'
st.write(title1, unsafe_allow_html=True)
user_input = st.text_input("",
                           placeholder="Type here")  # using st.text_input() to take user input for sentiment analysis

s = SentimentIntensityAnalyzer()  # Create a SentimentIntensityAnalyzer object.
score = s.polarity_scores(user_input)  # polarity_scores method of SentimentIntensityAnalyzer
# object gives a sentiment dictionary.
# which contains pos, neg, neu, and compound scores.


# decide sentiment as positive or negative

if score["compound"] <= - 0.05:
    new_title = '<p style="font-family:sans-serif; color:Red; font-size: 42px;">Negative</p>'
    st.markdown(new_title, unsafe_allow_html=True)

elif score["compound"]  >= 0.05:
    new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Positive</p>'
    st.markdown(new_title, unsafe_allow_html=True)
else:
    new_title = '<p style="font-family:sans-serif; color:Grey; font-size: 42px;">Neutral</p>'
    st.markdown(new_title, unsafe_allow_html=True)

# displaying a detailed result of sentiment analysis
st.write("Overall sentiment dictionary is : ", score)
st.write("sentence was rated as ", score['neg'] * 100, "% Negative")
st.write("sentence was rated as ", score['neu'] * 100, "% Neutral")
st.write("sentence was rated as ", score['pos'] * 100, "% Positive")
