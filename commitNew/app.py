from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load the model and tokenizer
model = tf.keras.models.load_model("sinhala_grammar_detection.h5")

# Load the tokenizer and set max length
tokenizer = Tokenizer()  # Ensure you save and load the same tokenizer used for training
max_len = 100  # Set based on your dataset

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/correct', methods=['POST'])
def correct():
    input_text = request.form['text']
    corrected_text = detect_and_correct(input_text, model, tokenizer, max_len)
    return jsonify({'corrected_text': corrected_text})

if __name__ == '__main__':
    app.run(debug=True)
