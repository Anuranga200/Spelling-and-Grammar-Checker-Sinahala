import pandas as pd
import re
from difflib import get_close_matches
import sys
import io
from indicnlp.tokenize import indic_tokenize
import Levenshtein
from difflib import get_close_matches

# Set the encoding to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

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
#print("Dictionary Loaded:", sinhala_dict)  # Debug print

# Step 2: Tokenize Sinhala text
def tokenize_sinhala_text(text):
    tokens = indic_tokenize.trivial_tokenize(text)
    print("Tokens:", tokens)  # Debug print
    return tokens

# Step 3: Correct spelling using the dictionary with get_close_matches
def correct_spelling_close_matches(word, dictionary):
    matches = get_close_matches(word, dictionary, n=1, cutoff=0.6)  # Set cutoff for similarity
    print(f"Word: {word}, Matches: {matches}")  # Debug print
    return matches[0] if matches else word

# Step 3: Correct spelling using the dictionary with Levenshtein distance
def correct_spelling_levenshtein(word, dictionary):
    closest_match = min(dictionary, key=lambda w: Levenshtein.distance(word, w))
    distance = Levenshtein.distance(word, closest_match)
    print(f"Word: {word}, Closest Match: {closest_match}, Distance: {distance}")  # Debug print
    return closest_match if distance < len(word) * 0.4 else word  # Adjust threshold as needed

# Main spelling correction function
def correct_text(text, method='close_matches'):
    words = tokenize_sinhala_text(text)
    if method == 'levenshtein':
        corrected_words = [correct_spelling_levenshtein(word, sinhala_dict) for word in words]
    else:
        corrected_words = [correct_spelling_close_matches(word, sinhala_dict) for word in words]
    return ' '.join(corrected_words)

# Test the function
input_text = """මගේ මවගේ නම කමලා. ඇය මට ඉගැනීමට උදව් කරන්නේය. ඇයට දිගු කොණ්ඩයක් ඇත. 
                අම්මා ගෙදර පිරිසිදුව තබා ගෙන සිටින්නීය. මගේ අම්මා හරිම කරුණාවන්තයි. අම්මා උදේම අවදි වන්නීය. 
                මම අම්මාට ගොඩක් ස්තූතී වන්ත වෙමු."""  # Intentional errors for testing
corrected_text_close_matches = correct_text(input_text, method='close_matches')
print("--------------------------------------------")
print("Corrected Text with close matches:", corrected_text_close_matches)
print("-------------SECOND METHOD------------------")

corrected_text_levenshtein = correct_text(input_text, method='levenshtein')
print("--------------------------------------------")
print("Corrected Text with Levenshtein:", corrected_text_levenshtein)