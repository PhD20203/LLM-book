# Grab the helper from Hugging Face to fetch our data
from datasets import load_dataset
# Pull in the main class to set up our tokenizer pipeline
from tokenizers import Tokenizer
# Get the Byte-Pair Encoding subword model architecture
from tokenizers.models import BPE
# Load the configuration tool needed to train BPE models
from tokenizers.trainers import BpeTrainer
# Use the basic rule to split text by blank spaces first
from tokenizers.pre_tokenizers import Whitespace

# Print a quick update so we know the downloading started
print("Loading WikiText dataset...")

# Fetch the raw wikitext-2 dataset directly from the web
dataset = load_dataset("wikitext", "wikitext-2-raw-v1")

# Extract just the text from the training part of the dataset
train_text = dataset["train"]["text"]

# Open a local file named wiki.txt to store this training text
with open("wiki.txt", "w", encoding="utf-8") as f:
    # Loop through each individual string in the training split
    for line in train_text:
        # Write the text line to the file and add a line break
        f.write(line + "\n")

# Initialize a clean, empty tokenizer object using the BPE model
tokenizer = Tokenizer(BPE())

# Tell the pipeline to handle word splitting by looking at spaces
tokenizer.pre_tokenizer = Whitespace()

# Set the maximum limit for our vocabulary file to 5000 tokens
trainer = BpeTrainer(vocab_size=5000)

# Run the training setup using the wiki.txt file we just created
tokenizer.train(["wiki.txt"], trainer)

# Set up a random test sentence to see how the model behaves
sentence = "Artificial Intelligence is changing the world."

# Pass our test string through the newly trained tokenizer pipeline
output = tokenizer.encode(sentence)

# Show a label indicating the clean, original string comes next
print("\nOriginal Sentence:")
# Print out the raw, unedited test sentence to the terminal
print(sentence)

# Show a label indicating the broken down tokens are next
print("\nBPE Tokens:")
# Output the final list of generated text subwords to the screen
print(output.tokens)
