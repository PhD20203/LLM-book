# Pull the smart tokenizer loader helper out from the transformers library
from transformers import AutoTokenizer

# Fire up the pretrained base settings for the multi-language cased BERT model
tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

# Set up a test string containing different languages to check translation handling
sentence = "Hello नमस्ते Bonjour こんにちは"

# Run our multi-language string through the model to break it into fragments
tokens = tokenizer.tokenize(sentence)

# Dump out the clean, unedited starting sentence onto our terminal monitor
print(sentence)

# Print the final array of subword tokens to see how it handled the text
print(tokens)
