import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the dataset
data_file = "sentences.txt"  # Replace with the actual file path
data = []

# Read the dataset line by line
with open(data_file, 'r', encoding='utf-8') as file:
    for line in file:
        label, sentence = line.strip().split(' ', 1)
        data.append((int(label), sentence))

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Label', 'Sentence'])

# Split into training and testing sets
train_sentences, test_sentences, train_labels, test_labels = train_test_split(
    df['Sentence'], df['Label'], test_size=0.2, random_state=42
)

# Tokenize the sentences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_sentences)

# Convert sentences to sequences
train_sequences = tokenizer.texts_to_sequences(train_sentences)
test_sequences = tokenizer.texts_to_sequences(test_sentences)

# Pad sequences to make them equal length
max_len = max(len(seq) for seq in train_sequences)
train_padded = pad_sequences(train_sequences, maxlen=max_len, padding='post')
test_padded = pad_sequences(test_sequences, maxlen=max_len, padding='post')
