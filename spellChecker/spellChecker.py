import pandas as pd
import re
from difflib import get_close_matches

# Step 1: Load Sinhala words from Excel
def load_dictionary_from_excel(file_path, column_name):
    # Read the Excel file
    df = pd.read_excel(file_path)
    # Extract the column with Sinhala words and convert to a list
    return df[column_name].dropna().tolist()

# Load the dictionary
file_path = "data-spell-checker.xlsx"  # Replace with the path to your Excel file
column_name = "word"  # Replace with the name of the column containing the words
sinhala_dict = load_dictionary_from_excel(file_path, column_name)

# Step 2: Tokenize Sinhala text
def tokenize_sinhala_text(text):
    return re.findall(r'\b\w+\b', text)

# Step 3: Correct spelling using the dictionary
def correct_spelling(word, dictionary):
    matches = get_close_matches(word, dictionary, n=1, cutoff=0.8)  # Set cutoff for similarity
    return matches[0] if matches else word

# Main spelling correction function
def correct_text(text):
    words = tokenize_sinhala_text(text)
    corrected_words = [correct_spelling(word, sinhala_dict) for word in words]
    return ' '.join(corrected_words)

# Test the function
input_text = "මම විදුලී සංගීටය අගනාගයි"  # Intentional errors for testing
corrected_text = correct_text(input_text)
print("Corrected Text:", corrected_text)
