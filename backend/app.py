from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import pipeline
import torch

app = Flask(__name__)
CORS(app)

# Load the emotion analysis pipeline
emotion_model = pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    if not text.strip():
        return jsonify({'error': 'No text provided'}), 400

    try:
        result = emotion_model(text)[0][0]
        emotion = result['label']
        confidence = round(result['score'], 2)
        return jsonify({'emotion': emotion, 'confidence': confidence})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
