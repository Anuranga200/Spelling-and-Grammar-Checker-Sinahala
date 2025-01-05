import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QWidget
from PyQt5.QtCore import Qt

def check_grammar():
    sentence = input_box.toPlainText()
    sentence_clean = preprocess_text(sentence)
    features = vectorizer.transform([sentence_clean])
    prediction = model.predict(features)[0]

    issues = grammar_rules_check(sentence)

    if prediction == 1 and not issues:
        result_label.setText("The sentence is grammatically correct.")
    else:
        result_label.setText(f"The sentence has issues: {'; '.join(issues)}")

# GUI Setup
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Sinhala Grammar Checker')
layout = QVBoxLayout()

instructions_label = QLabel("Enter a Sinhala paragraph below:")
instructions_label.setAlignment(Qt.AlignLeft)
layout.addWidget(instructions_label)

input_box = QTextEdit()
layout.addWidget(input_box)

check_button = QPushButton("Check Grammar")
check_button.clicked.connect(check_grammar)
layout.addWidget(check_button)

result_label = QLabel("")
layout.addWidget(result_label)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
