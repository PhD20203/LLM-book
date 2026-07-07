# Pull in the sentencepiece package helper as sp to handle our text segmentation
import sentencepiece as sp

# Set up the short sample string that we want to chop into subword tokens
sentence = "Artificial Intelligence"

# Fire up the encoder method to split our text into clean, readable string fragments
print(sp.encode(sentence, out_type=str))
