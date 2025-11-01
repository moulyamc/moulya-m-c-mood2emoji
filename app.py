import streamlit as st
from textblob import TextBlob

BAD_WORDS = ["stupid", "hate", "kill", "idiot", "dumb"]

def clean_text(text):
    for word in BAD_WORDS:
        if word in text.lower():
            return False
    return True

def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return "😀", "Sounds happy!"
    elif polarity < -0.1:
        return "😞", "Sounds a bit sad."
    else:
        return "😐", "Sounds neutral."

st.set_page_config(page_title="Mood2Emoji", page_icon="😀")

st.title("Mood2Emoji 🧠✨")
st.write("Type a short sentence and I’ll guess the mood (safely!).")

text_input = st.text_input("Your sentence:")

if text_input:
    if not clean_text(text_input):
        st.warning("⚠️ Please use kind and appropriate words.")
    else:
        emoji, explanation = analyze_mood(text_input)
        st.markdown(f"## {emoji} {explanation}")

with st.expander("👩‍🏫 Teacher Mode"):
    st.subheader("How it works")
    st.write("""
    1. The app reads your sentence.
    2. It checks for kind and safe language.
    3. Using **TextBlob**, it measures how positive or negative the sentence feels.
    4. Based on that, it shows an emoji and a short message.
    """)

st.caption("Kid-safe Mood Detector © 2025 | Built by Moulya M C")
