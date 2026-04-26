import json

# import re
from flask import Flask, jsonify, render_template, request
from google import genai
from google.genai import types

app = Flask(__name__)

# --- HARDCODED KEY ---
GEMINI_API_KEY = "AIzaSyBJF_34NrVQZ4b4nTgMuE32bjhMCohyOto"

# Strict System Prompt for the AEO Engine
SYS_PROMPT = """You are an elite AEO (Answer Engine Optimization) strategist.
Respond ONLY with valid JSON.
Schema:
{
  "aeo_score_before": <int>,
  "aeo_score_after": <int>,
  "ranking_prediction": "<string>",
  "snippet_type": "<string>",
  "optimized_content": "<string>",
  "improvements": [{"category": "<string>", "change": "<string>", "impact": "<string>"}],
  "keywords_added": ["<string>"],
  "top_tip": "<string>"
}"""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/optimize", methods=["POST"])
def optimize():
    data = request.json
    content = data.get("content")
    query = data.get("query")

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            config=types.GenerateContentConfig(
                system_instruction=SYS_PROMPT, response_mime_type="application/json"
            ),
            contents=[f"Target Query: {query}\n\nContent:\n{content}"],
        )

        if not response.text:
            return jsonify({"error": "No response from AI."}), 400

        # Parse and return JSON
        return jsonify(json.loads(response.text))

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
