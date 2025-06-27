# app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load .env and setup Gemini
load_dotenv()
from ai_pipeline.ai_writer import ai_writer_gemini

app = Flask(__name__, static_folder="web_output", static_url_path="")
CORS(app)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/api/spin", methods=["POST"])
def spin():
    data = request.get_json()
    prompt = data.get("text", "")
    try:
        spun_text = ai_writer_gemini(prompt)
        return jsonify({"spun": spun_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
