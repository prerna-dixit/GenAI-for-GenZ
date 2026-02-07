# 🏗️ System Architecture

This document describes the architecture of the **GenAI Documentation Agent**.

---

## 🔍 Overview

The application follows a **simple client–server architecture**, separating the user interface from the AI-powered processing logic.

The system is designed to be:
- lightweight
- modular
- easy to deploy
- easy to extend in the future

---

## 🧩 Architecture Diagram (Conceptual)

# 🏗️ System Architecture

This document describes the architecture of the **GenAI Documentation Agent**.

---

## 🔍 Overview

The application follows a **simple client–server architecture**, separating the user interface from the AI-powered processing logic.

The system is designed to be:
- lightweight
- modular
- easy to deploy
- easy to extend in the future

---

## 🧩 Architecture Diagram (Conceptual)

        [ User Browser ]
             |
             v
  [ Frontend (HTML/CSS/JS) ]
             |
             v
   [ Flask Backend API ]
             |
             v
[ GenAI Text Processing Logic ]


---

## 🖥️ Frontend Layer

**Responsibilities:**
- Collect user input (long documents)
- Send input to backend API
- Display reduced output
- Provide a calm, cozy, distraction-free UI

**Technologies Used:**
- HTML
- CSS
- JavaScript

The frontend is designed to be static and deployment-friendly, making it suitable for platforms like Netlify.

---

## ⚙️ Backend Layer

**Responsibilities:**
- Receive text input via API requests
- Process text using GenAI-based semantic compression
- Return reduced content as JSON

**Technologies Used:**
- Python
- Flask

The backend exposes a single main endpoint:


---

## 🖥️ Frontend Layer

**Responsibilities:**
- Collect user input (long documents)
- Send input to backend API
- Display reduced output
- Provide a calm, cozy, distraction-free UI

**Technologies Used:**
- HTML
- CSS
- JavaScript

The frontend is designed to be static and deployment-friendly, making it suitable for platforms like Netlify.

---

## ⚙️ Backend Layer

**Responsibilities:**
- Receive text input via API requests
- Process text using GenAI-based semantic compression
- Return reduced content as JSON

**Technologies Used:**
- Python
- Flask

The backend exposes a single main endpoint:

POST /generate


which accepts raw text and returns the compressed version.

---

## 🧠 AI Processing Logic

The AI component focuses on **semantic reduction**, not summarization.

Key design principles:
- Preserve meaning and intent
- Remove redundancy
- Avoid over-simplification
- Produce human-readable output

This logic is intentionally modular so that:
- different LLMs can be swapped in
- compression strategies can be tuned later

---

## 🚀 Deployment Strategy

The system supports **split deployment**:

- **Frontend** → Static hosting (e.g., Netlify)
- **Backend** → Python-compatible hosting (e.g., Render)

This separation improves scalability and simplifies maintenance.

---

## 🌱 Future Extensions

- File uploads (PDF / DOCX)
- Adjustable compression levels
- Authentication for saved documents
- Multi-language support

---

This architecture prioritizes clarity, usability, and extensibility over unnecessary complexity.
