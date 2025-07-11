# 🎭 Emotion Analyzer App

A simple full-stack application that analyzes the emotion behind your written reflections. Built with **React** on the frontend and **Flask + Transformers + PyTorch** on the backend.

---

## 📌 Features

- Enter any text and detect its underlying emotion
- Uses state-of-the-art NLP model from Hugging Face
- Clean, responsive interface built with React
- Lightweight Flask backend powered by PyTorch

---

## 🧱 Tech Stack

### Frontend:
- React.js (Create React App)
- CSS (or Tailwind optional)
- `fetch()` API for requests

### Backend:
- Flask
- Hugging Face Transformers (`j-hartmann/emotion-english-distilroberta-base`)
- PyTorch
- flask-cors

---

## 📂 Folder Structure


---

## ⚙️ Prerequisites

Make sure you have these installed:

- [Node.js & npm](https://nodejs.org/)
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/) (optional)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/emotion-analyzer.git
cd emotion-analyzer
```

# 🖥️ Running the Frontend (React App)
## Step-by-step:

### 1.Navigate to the frontend folder:

```` bash
cd frontend  
````
### 2.Install frontend dependencies:

```bash
npm install
```
### 3.Start the React development server:
``` bash
npm start
```
This will start the frontend at:

```arduino
http://localhost:3000
```

# 🧪 Running the Backend (Flask + Transformers)
## Step-by-step:
### 1.Open a new terminal and go to the backend folder:

```bash
cd backend
```
### 2.(Optional) Create a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```
### 3.Install backend dependencies:
```bash
pip install -r requirements.txt
```
### 4.Start the Flask server:
```bash
python app.py
```
### 5.This will start the backend at:

```arduino
http://localhost:5000
```
# 🔄 How Frontend Talks to Backend
## The frontend uses the fetch API to send a POST request to the backend:

```js

fetch("http://localhost:5000/predict", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ text })
})
```
#### Expected backend response:

```json
{
  "emotion": "Joy"
}
```
## 💬 Example Input & Output
#### Input:

``` css

I feel very happy today because I accomplished my goals!
```
### Output:

```yaml
Detected Emotion: Joy 😊
```

# 🧪 Test Sentences
* Try these inputs to test the model:

* "I’m feeling fantastic and proud."

* "Why is everything so frustrating?"

* "I feel sad and lonely."

* "I'm terrified about what might happen."

* "It's been a calm and peaceful day."


# ❗ Troubleshooting
## 1. CORS Error
### Make sure this is added in app.py:

```python
from flask_cors import CORS
CORS(app)
```
## 2. Backend Not Responding?
* Ensure python app.py is running

* Flask should run on port 5000

* Check if firewall/antivirus is blocking local ports

### 3. Frontend Not Showing Result?
* Make sure API endpoint is http://localhost:5000/predict

* Both frontend (:3000) and backend (:5000) must run simultaneously

# 📘 License
### MIT License — free for personal and commercial use.

## 🙌 Acknowledgments
* Hugging Face Transformers

* PyTorch

* Flask

* React
