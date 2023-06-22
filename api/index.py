from flask import Flask, jsonify
import gdown

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message='hi')

@app.route('/about')
def about():
    return 'About'
    
@app.route('/run-colab')
def run_colab():
    gdown.download('https://colab.research.google.com/drive/1uf0ZjX-uqJC6LaObRUZpfdQI7TYqkTN-', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
