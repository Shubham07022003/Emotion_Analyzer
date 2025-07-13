import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()  # Loads variables from .env

HF_TOKEN = os.environ.get("HF_TOKEN")

print("HF_TOKEN:", HF_TOKEN)


app = Flask(__name__)
CORS(app)


# Initialize the client with model and token
client = InferenceClient(
    model="j-hartmann/emotion-english-distilroberta-base",
    token=HF_TOKEN
)



@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    if not text.strip():
        return jsonify({'error': 'No text provided'}), 400

    try:
        results = client.text_classification(text)
        result = results[0]
        return jsonify({
            'emotion': result['label'],
            'confidence': round(result['score'], 2)
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
