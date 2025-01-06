# Sinhala Spelling and Grammar Checker

A tool designed to automatically correct spelling errors and suggest grammar corrections for Sinhala text. This project leverages AI-based approaches to improve the accuracy and readability of written Sinhala, focusing on both spelling and contextual grammar issues.

---

## Features

- **Spelling Correction**:
  - Identifies and corrects common spelling mistakes.
  - Provides up to 5 spelling suggestions for unrecognized words.
  - Uses Levenshtein distance for error detection and correction.

- **Grammar Suggestions**:
  - Corrects contextual agreement errors (e.g., verb-subject agreement).
  - Fixes word order issues to ensure proper syntax in Sinhala sentences.

- **Accuracy**:
  - Spelling Correction: 88%
  - Grammar Suggestions: 83%

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - [Levenshtein](https://github.com/ztane/python-Levenshtein) - For spelling distance calculations.
  - [Pandas](https://pandas.pydata.org/) - For handling word datasets.
  - [Gradio](https://gradio.app/) - For creating an interactive user interface.
  - [Google Generative AI](https://developers.generativeai.google) - For advanced text processing (if applicable).

---

## How It Works

1. **Spell Checker**:
   - Splits the input text into words using Sinhala-specific tokenization.
   - Compares each word against a pre-defined dictionary of correct words.
   - Suggests corrections for misspelled words based on similarity.

2. **Grammar Checker**:
   - Analyzes the text for predefined grammatical errors.
   - Applies rule-based corrections for subject-verb agreement and word order.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sinhala-spelling-grammar-checker.git
   cd sinhala-spelling-grammar-checker
