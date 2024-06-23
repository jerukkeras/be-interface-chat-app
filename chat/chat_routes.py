import json

import google.generativeai as genai
from flask import Blueprint, jsonify, request

# 🔥🔥 FILL THIS OUT FIRST! 🔥🔥
# Get your Gemini API key by:
# - Selecting "Add Gemini API" in the "Project IDX" panel in the sidebar
# - Or by visiting https://g.co/ai/idxGetGeminiKey
API_KEY = 'AIzaSyAnoCicIuiRrHzJp2rK7r3TWSsbNNK998w'

genai.configure(api_key=API_KEY)

chat = Blueprint('chat', __name__)


@chat.route("/api/generate", methods=["POST"])
def generate_api():
    if request.method == "POST":
        if API_KEY == 'TODO':
            return jsonify({"error": '''
                To get started, get an API key at
                https://g.co/ai/idxGetGeminiKey and enter it in
                main.py
                '''.replace('\n', '')})
        try:
            req_body = request.get_json()
            content = req_body.get("contents")
            model = genai.GenerativeModel(model_name=req_body.get("model"))
            chat_model = model.start_chat(history=[])
            response = chat_model.send_message(content, stream=True)

            def stream():
                for chunk in response:
                    yield 'data: %s\n\n' % json.dumps({"text": chunk.text})

            return stream(), {'Content-Type': 'text/event-stream'}

        except Exception as e:
            return jsonify({"error": str(e)})
