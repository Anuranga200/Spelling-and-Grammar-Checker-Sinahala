import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset from .txt File
def load_txt_dataset(file_path):
    sentences = []
    labels = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            label, sentence = line.strip().split(' ', 1)  # Split into label and sentence
            labels.append(int(label))  # Convert label to integer
            sentences.append(sentence)  # Append sentence
    return pd.DataFrame({'sentence': sentences, 'is_correct': labels})

# Preprocess Sinhala Sentences
def preprocess_text(text):
    # Remove unwanted characters like punctuation
    text = re.sub(r'[!@#$%^&*()_+=\[\]{};:"\\|,.<>?/0-9]', '', text)
    text = text.strip()
    return text

# Feature Extraction (Bag of Words)
def extract_features(sentences):
    vectorizer = CountVectorizer(analyzer='char', ngram_range=(1, 3))  # Character-level n-grams
    features = vectorizer.fit_transform(sentences)
    return features, vectorizer

# Train Model
def train_model(features, labels):
    model = MultinomialNB()
    model.fit(features, labels)
    return model

# Evaluate Model
def evaluate_model(model, features, labels):
    predictions = model.predict(features)
    accuracy = accuracy_score(labels, predictions)
    print("Accuracy:", accuracy)
    print("Classification Report:\n", classification_report(labels, predictions))

# Rule-Based Grammar Check
def grammar_rules_check(sentence):
    issues = []
    if not sentence.endswith(('.', '!', '?')):
        issues.append("Sentence should end with a proper punctuation mark.")
    if sentence.startswith(' '):
        issues.append("Sentence should not start with a space.")
    # Add more rules as needed
    return issues

# Main Execution
if __name__ == "__main__":
    # Load Data from .txt File
    file_path = 'sentences.txt'  # Path to your dataset file
    data = load_txt_dataset(file_path)
    data['sentence'] = data['sentence'].apply(preprocess_text)

    # Split Dataset
    X_train, X_test, y_train, y_test = train_test_split(data['sentence'], data['is_correct'], test_size=0.2, random_state=42)

    # Extract Features
    X_train_features, vectorizer = extract_features(X_train)
    X_test_features = vectorizer.transform(X_test)

    # Train and Evaluate Model
    model = train_model(X_train_features, y_train)
    evaluate_model(model, X_test_features, y_test)

    # Test Rule-Based Check
    test_sentence = "මම පාසල් ගියෙමි"
    issues = grammar_rules_check(test_sentence)
    if issues:
        print("Grammar Issues:", issues)
    else:
        print("No grammar issues detected.")