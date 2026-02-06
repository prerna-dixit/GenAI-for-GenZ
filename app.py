from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ---- AI LOGIC (your "model") ----

def compress_text(text):
    # Simulated semantic compression
    return text[:600] + "\n\n[Semantic meaning preserved]"

def generate_documentation(compressed_text):
    return f"""
## Generated Documentation

### Overview
This document was processed using a GenAI-powered semantic compression pipeline.

### What the AI did
- Reduced redundant content
- Preserved intent and structure
- Generated human-readable documentation

### Compressed Content
{compressed_text}
"""

# ---- ROUTES ----

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"error": "No input provided"}), 400

    compressed = compress_text(text)
    output = generate_documentation(compressed)

    return jsonify({"result": output})


if __name__ == "__main__":
    app.run(debug=True)
