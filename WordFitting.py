# Pull down the general tokenizer configuration helper from our transformers tool
from transformers import AutoTokenizer

# Fire up the base uncased version setup specifically for the BERT model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Create a clean array containing a few sample text items we want to test out
words = [
    # A standard verb with a normal suffix ending to track fragmenting
    "playing",
    # An adjective using a prefix to see how the model splits it up
    "unbelievable",
    # A technical engineering phrase with a common structural suffix layout
    "tokenization",
    # A descriptive word to check how the tokenizer processes compound segments
    "friendliness"
]

# Start looping through each individual string item inside our words collection
for word in words:
    # Spit out the original string along with its newly broken subword fragments
    print(word, "->", tokenizer.tokenize(word))
