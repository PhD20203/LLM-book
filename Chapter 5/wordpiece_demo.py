# Grab the function from Hugging Face to load our online datasets
from datasets import load_dataset
# Pull down the specific tokenizer class built for processing BERT models
from transformers import BertTokenizer

# Print out a status update so we know the process is moving
print("Loading IMDB Dataset...")

# Fetch the complete movie review dataset directly from the web portal
dataset = load_dataset("imdb")

# Load up the standard pre-trained layout config for the basic uncased BERT model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Extract the raw text string from the very first row of our training set
sentence = dataset["train"][0]["text"]

# Run the text data through our tokenizer to break it into individual subwords
tokens = tokenizer.tokenize(sentence)

# Output a header label indicating that the clean original string is next
print("\nOriginal Sentence:\n")
# Slice and print out just the first 300 characters of the movie review text
print(sentence[:300])

# Output a header label indicating that the processed tokens are next
print("\nWordPiece Tokens:\n")
# Grab just the first 100 subword tokens from our array to show on screen
print(tokens[:100])
