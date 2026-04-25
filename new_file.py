import os
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
from flask import Flask, render_template_string, request
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

# --- CONFIGURATION ---
API_KEY = 'AIzaSyAK_Be4mNoGC__mbWsVMml67sf2AIm90hg'
genai.configure(api_key=API_KEY)
# Using Gemini 3 Flash for speed and AEO logic
model = genai.GenerativeModel('gemini-3-flash-preview')

# HTML Template (Everything in one file for easy copy-paste)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AEO Optimizer</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
    <style>
        body { background-color: #f5f7fa; padding: 40px; }
        .result-box { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-top: 20px; }
        pre { background: #2d3436; color: #fab1a0; padding: 15px; border-radius: 5px; overflow-x: auto; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title has-text-centered">🚀 AEO Website Optimizer</h1>
        <div class="box">
            <form method="POST">
                <div class="field has-addons">
                    <div class="control is-expanded">
                        <input class="input" type="text" name="url" placeholder="https://example.com" required>
                    </div>
                    <div class="control">
                        <button class="button is-link" type="submit">Optimize</button>
                    </div>
                </div>
            </form>
        </div>

        {% if result %}
        <div class="result-box">
            <h2 class="subtitle">Optimization Results for: <strong>{{ url }}</strong></h2>
            <div class="content">
                {{ result | safe }}
            </div>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    url = None
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            
            resp = requests.get(url, headers=headers, timeout=10, verify=False)
            soup = BeautifulSoup(resp.text, 'html.parser')
            
            # 1. REMOVE THE NOISE
            # This deletes the stuff that distracts the AI
            for noise in soup(["script", "style", "nav", "footer", "header", "aside"]):
                noise.decompose()
            
            # 2. TARGET THE "MEAT"
            # We look for common main content containers first
            main_content = soup.find('main') or soup.find('article') or soup.find('div', id='content') or soup.body
            
            if main_content:
                # Extracting only descriptive tags to give AI better context
                text_elements = main_content.find_all(['h1', 'h2', 'p', 'li'])
                text = " ".join([t.get_text(strip=True) for t in text_elements])[:5000]
            else:
                text = soup.get_text(separator=' ', strip=True)[:5000]

            # 3. REFINED AI PROMPT
            # Tell the AI to ONLY focus on the core service/product found in the text
            prompt = f"""
            System Role: You are a highly precise Data Extraction Engine. Your goal is to process the provided URL/Image/Text and extract core information while ignoring UI elements, navigation bars, advertisements, and placeholder templates.

            Instructions:

            Identify the Core Subject: Determine the primary topic of the content (e.g., a political discussion, a technical article, or a product page).

            Text Extraction: Summarize the main arguments, facts, or data points presented.

            Visual Analysis: If images or screenshots are present, describe only the elements that contribute to the narrative. Ignore decorative icons or layout graphics.

            Sentiment/Context: Identify the tone and the specific audience being addressed.

            Noise Reduction: Do not include "About Us," "Terms of Service," "Related Posts," or technical SEO metadata unless specifically asked.

            Output Format:

            Primary Subject: [One sentence]

            Key Findings/Data Points: [Bullet points]

            Visual Context: [Description of relevant imagery]

            Tone/Sentiment: [Brief analysis]

            Raw Extracted Text: [Cleaned version of the essential text only]

            Constraint: If the input contains "Placeholder" or "Example" text (like B2B SaaS templates), ignore them and focus exclusively on the user-submitted content.
            Website Text: {text}
            
            Format as:
            <h3>Target Intent</h3> (Explain what the site actually does)
            <h3>AI Summary</h3> (The 50-word answer box snippet)
            <h3>FAQ Schema</h3> (The JSON-LD code block)
            """
            
            ai_response = model.generate_content(prompt)
            result = ai_response.text.replace('```json', '<pre>').replace('```', '</pre>')
        except Exception as e:
            result = f"<p class='has-text-danger'>Error: {str(e)}</p>"
            
    return render_template_string(HTML_TEMPLATE, result=result, url=url)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
