def correct_sentence(sentence):
    corrections = {
        "දෙන්නේය": "දෙයි",
        "කරන්නේය": "කරණුයේ",
        "වෙමු": "වෙමි",
    }
    for incorrect, correct in corrections.items():
        if incorrect in sentence:
            sentence = sentence.replace(incorrect, correct)
    return sentence

# Example usage
test_sentence = "මම අම්මාට ගොඩක් ස්තූතී වන්ත වෙමු."
corrected_sentence = correct_sentence(test_sentence)
print(corrected_sentence)
