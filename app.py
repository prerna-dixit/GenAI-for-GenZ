from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ---- AI LOGIC (your "model") ----


import re

def compress_text(text, max_sentences=4):
    # split by lines first
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    cleaned_lines = []
    for line in lines:
        words = line.split()

        # skip heading-like lines (short, title-like, no punctuation)
        if (
            len(words) <= 6 and
            not re.search(r'[.!?]', line)
        ):
            continue

        cleaned_lines.append(line)

    # now normalize spacing AFTER removing headings
    text = " ".join(cleaned_lines)

    # split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    compressed = []
    for s in sentences:
        s = s.strip()

        if len(s) < 50:
            continue

        if s.lower().startswith(("the document", "this document")):
            continue

        compressed.append(s)

        if len(compressed) >= max_sentences:
            break

    return " ".join(compressed)










def generate_documentation(compressed_text):
    return compressed_text

# ---- ROUTES ----

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json(force=True)
        text = data.get("text", "")

        if not text.strip():
            return jsonify({"error": "No input provided"}), 400

        compressed = compress_text(text)
        output = generate_documentation(compressed)

        return jsonify({"result": output})

    except Exception as e:
        print("SERVER ERROR:", e)
        return jsonify({"error": "Internal server error"}), 500


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

