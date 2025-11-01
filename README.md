# Mood2Emoji 🧠😀  
A kid-safe text mood detector for students aged 12–16.

## 🌟 What it does
This app takes a short sentence, checks if it’s kind and appropriate, then uses **TextBlob** to find the mood — happy, sad, or neutral.  
It returns an emoji and a short explanation like “Sounds happy!”  

Optional **Teacher Mode** shows a simple diagram of how it works.

---

## 🧩 Tech Used
- Python 3.9+
- Streamlit
- TextBlob

---

## 🧠 How Kids Learn From It
Students learn:
- How apps can read and interpret text.
- Basic *sentiment analysis* with TextBlob.
- Safe coding practices (filtering bad words).
- Building and sharing apps using Streamlit.

---

## ⏰ How to Teach in 60 Minutes

| Time | Activity | Description |
|------|-----------|-------------|
| 0–10 min | Intro | Explain what sentiment/mood detection means |
| 10–25 min | Code Walkthrough | Show `app.py` logic step by step |
| 25–40 min | Hands-on | Students type sentences and observe emoji results |
| 40–50 min | Modify | Let them add their own positive/negative words |
| 50–60 min | Recap | Discuss what the app did and how TextBlob helped |

---

## 🧩 Setup Instructions
1. Clone the repo:
   ```bash
   git clone https://github.com/moulya-m-c-mood2emoji.git
   cd moulya-m-c-mood2emoji
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 🌍 Streamlit Deployment
- Go to [streamlit.io/cloud](https://streamlit.io/cloud)
- Sign in → “New App”
- Connect your GitHub repo → select branch → deploy!

---

## ⚙️ Known Limitations
- TextBlob may misclassify sarcasm.
- Works best with English text.
- Limited word filter (can be expanded for safety).

---

## 📜 License
Free for educational use.  
Made by **Moulya M C** for the Curriculum Developer Intern assignment.
