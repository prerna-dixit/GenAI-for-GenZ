# 🐱 GenAI Documentation Agent

A GenAI-powered web application that reduces long documents while preserving their original meaning and context — presented through a calm, cozy, notebook-inspired interface.

This project focuses on **semantic reduction**, not aggressive summarization, helping users understand long text faster without losing important ideas.

---

## 🌸 Live Demo (Use This)

🔗 **https://genai-for-genz.onrender.com**

👉 This is the primary way to use the project.  
No installation or setup is required.

> Note: The app is hosted on a free tier. The first request may take a few seconds due to cold start.

---

## ✨ What This Project Does

The GenAI Documentation Agent takes long-form text such as:
- reports  
- documentation  
- notes  
- articles  

and produces a **reduced version** that:
- removes redundancy  
- preserves intent and meaning  
- avoids over-simplification  
- remains human-readable  

The goal is **clarity**, not just shortening.

---

## 🧠 Why This Exists

In academic and professional settings, users often face:
- information overload  
- repeated explanations  
- long documents that are hard to scan  

Many summarization tools remove too much context or feel unreliable.  
This project explores a gentler alternative: **semantic compression** — keeping what matters while removing what doesn’t.

---

## 🎨 Design Philosophy

The interface is intentionally designed to feel:
- calm
- cozy
- non-intimidating

Inspired by:
- notebook paper textures  
- soft color palettes  
- kawaii / anime-style doodles  
- jujutsu kaisen gojo satoru doodles

The goal is to make interacting with AI feel **human and approachable**, not overwhelming or overly technical.
Also contains my name Prerna, in japanese[katakana] at the top left corner.
Has cat and star doodles.
Has jujutsu kaisen kawaii doodles.
Has sakura leaves falling.

---

## 🧩 System Architecture (High-Level)

# 🐱 GenAI Documentation Agent

A GenAI-powered web application that reduces long documents while preserving their original meaning and context — presented through a calm, cozy, notebook-inspired interface.

This project focuses on **semantic reduction**, not aggressive summarization, helping users understand long text faster without losing important ideas.

---

## 🌸 Live Demo (Use This)

🔗 **https://genai-for-genz.onrender.com**

👉 This is the primary way to use the project.  
No installation or setup is required.

> Note: The app is hosted on a free tier. The first request may take a few seconds due to cold start.

---

## ✨ What This Project Does

The GenAI Documentation Agent takes long-form text such as:
- reports  
- documentation  
- notes  
- articles  

and produces a **reduced version** that:
- removes redundancy  
- preserves intent and meaning  
- avoids over-simplification  
- remains human-readable  

The goal is **clarity**, not just shortening.

---

## 🧠 Why This Exists

In academic and professional settings, users often face:
- information overload  
- repeated explanations  
- long documents that are hard to scan  

Many summarization tools remove too much context or feel unreliable.  
This project explores a gentler alternative: **semantic compression** — keeping what matters while removing what doesn’t.

---

## 🎨 Design Philosophy

The interface is intentionally designed to feel:
- calm
- cozy
- non-intimidating

Inspired by:
- notebook paper textures  
- soft color palettes  
- kawaii / anime-style doodles  

The goal is to make interacting with AI feel **human and approachable**, not overwhelming or overly technical.

---

## 🧩 System Architecture (High-Level)

         User Browser
               ↓
Frontend (HTML / CSS / JavaScript)
               ↓
      Flask Backend API
               ↓
    GenAI Text Reduction Logic



The backend exposes a single main endpoint:

POST /generate


which accepts raw text and returns the reduced version.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **AI Logic:** GenAI-based semantic text reduction  
- **Deployment:** Render (full-stack)

---

## 📌 How to Use

1. Open the live demo link  
2. Paste a document into the input box  
3. Click **Generate Reduced Version**  
4. Read the compressed output below  

The output focuses only on essential ideas and does not expose internal AI steps.

---

## 🧪 Running Locally (Optional)

This section is **only for developers** who want to explore or extend the project.

```bash
git clone https://github.com/your-username/genai-for-genz.git
cd genai-for-genz
pip install flask
python app.py

Then open:
http://127.0.0.1:5000

-- 🌱 Future Improvements

File upload support (PDF / DOCX)

Adjustable compression levels

Export reduced text as Markdown or TXT

Improved mobile responsiveness

Multi-language support




💗 Author

Built with care by Prerna
プレルナ