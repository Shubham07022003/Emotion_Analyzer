# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

## Emotion Reflection Analyzer

This is a simple web app where users can enter a short text reflection (e.g., “I feel nervous about my first job interview”), send it to a Python backend API that returns a mock “emotion analysis,” and display that result nicely in the frontend.

### How to Run

#### 1. Start the Flask Backend
- Go to the `backend` directory (create it if it doesn't exist).
- Create a Python virtual environment and install Flask:
  ```bash
  python -m venv venv
  venv\Scripts\activate  # On Windows
  pip install Flask flask-cors
  ```
- Create `app.py` (see below for code).
- Run the backend:
  ```bash
  flask run
  ```

#### 2. Start the React Frontend
- In another terminal, go to the `my-app` directory.
- Install dependencies (if not already):
  ```bash
  npm install
  ```
- Start the React app:
  ```bash
  npm start
  ```

The React app will be available at http://localhost:3000 and will communicate with the Flask backend at http://localhost:5000.

---

### Flask Backend Example (`backend/app.py`):
```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    # Fake analysis logic
    emotions = ['Happy', 'Sad', 'Anxious', 'Excited', 'Calm', 'Angry']
    emotion = random.choice(emotions)
    confidence = round(random.uniform(0.7, 0.99), 2)
    return jsonify({'emotion': emotion, 'confidence': confidence})

if __name__ == '__main__':
    app.run(debug=True)
