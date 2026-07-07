# Pull the universal tokenizer constructor helper from the transformers library
from transformers import AutoTokenizer

# Fire up the default pre-trained config path for the uncased BERT model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Set up a quick sample text string to test out the tokenizer settings
sentence = "Artificial Intelligence is changing the world."

# Pass our sample text sentence into the tool to split it into word fragments
tokens = tokenizer.tokenize(sentence)

# Print a simple label indicating the clean original text is coming up next
print("Original Sentence:")
# Output the raw, unmodified sample string onto our console screen
print(sentence)

# Print out a newline followed by a label for our processed output list
print("\nTokens:")
# Spit out the final array of subword tokens to verify the breakdown
print(tokens)
