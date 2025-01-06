import tkinter as tk
from tkinter import scrolledtext
from spelling_grammar import correct_text

def process_text():
    # Get input from the text box
    input_text = input_box.get("1.0", tk.END).strip()
    if not input_text:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter some text.")
        return
    
    # Correct the text
    corrected_text = correct_text(input_text)
    
    # Display the output
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, corrected_text)

# GUI setup
root = tk.Tk()
root.title("Sinhala Spelling and Grammar Checker")
root.geometry("600x400")

# Input label and box
input_label = tk.Label(root, text="Enter your Sinhala text:")
input_label.pack(pady=5)

input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
input_box.pack(pady=10)

# Correct button
correct_button = tk.Button(root, text="Correct Text", command=process_text)
correct_button.pack(pady=10)

# Output label and box
output_label = tk.Label(root, text="Corrected text:")
output_label.pack(pady=5)

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
output_box.pack(pady=10)

# Run the GUI
root.mainloop()
