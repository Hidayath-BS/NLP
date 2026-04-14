import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

def word_freq(text):
    """
    top 20 common words and their frequencies
    """
    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = Counter(words)

    plt.figure(figsize=(10, 6))
    plt.bar(*zip(*word_freq.most_common(20)))
    plt.title('Top 20 Common Words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()

def word_length(text):
    """
    distribution of word lengths
    """
    words = re.findall(r'\b\w+\b', text.lower())
    word_lengths = [len(w) for w in words]

    plt.figure(figsize=(10, 6))
    sns.histplot(word_lengths, bins=10, kde=True, color='skyblue')
    plt.title('Word Length Distribution')
    plt.xlabel('Word Length')
    plt.ylabel('Density')
    plt.show()

def char_level(text):
    """
    character frequency distribution
    """
    chars = re.findall(r'\S', text.lower())
    char_freq = Counter(chars)

    top_char = char_freq.most_common(15)
    labels, values = zip(*top_char)
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='salmon')
    plt.title('Top 20 Character Frequencies')
    plt.xlabel('Characters')
    plt.ylabel('Frequency')
    plt.show()

    letters = {k: v for k, v in char_freq.items() if k.isalpha()}
    punct = {k: v for k, v in char_freq.items() if not k.isalnum()}

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.bar(*zip(*Counter(letters).most_common(10)), color='green')
    plt.title("Letters")

    plt.subplot(1, 2, 2)
    plt.bar(*zip(*Counter(punct).most_common(10)), color='red')
    plt.title("Punctuation")

    plt.show()

def sentence_length(text):
    """
    distribution of sentence lengths
    """
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    sent_lengths = [len(re.findall(r'\b\w+\b', s)) for s in sentences]

    plt.figure(figsize=(10, 6))
    sns.boxenplot(sent_lengths, color='lightgreen')
    plt.title('Sentence Length Distribution')
    plt.xlabel('Sentence Length (in words)')
    plt.show()

def create_dashboard(text):
    """
    create a dashboard with all visualizations
    """
    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = Counter(words)

    # Word lengths
    word_lengths = [len(w) for w in words]

    # Characters (excluding spaces)
    chars = re.findall(r'\S', text.lower())
    char_freq = Counter(chars)

    # Sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    sent_lengths = [len(re.findall(r'\b\w+\b', s)) for s in sentences]

    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # --- Top-left: Word Frequency ---
    top_words = word_freq.most_common(10)
    labels, values = zip(*top_words)

    axs[0, 0].barh(labels, values, color='skyblue')
    axs[0, 0].invert_yaxis()
    axs[0, 0].set_title("Top Words")

    # --- Top-right: Word Length ---
    sns.histplot(word_lengths, bins=10, kde=True, ax=axs[0, 1], color='purple')
    axs[0, 1].set_title("Word Length Dist.")

    # --- Bottom-left: Character Frequency ---
    top_chars = char_freq.most_common(10)
    axs[1, 0].bar(*zip(*top_chars), color='orange')
    axs[1, 0].set_title("Top Characters")

    # --- Bottom-right: Sentence Length ---
    sns.boxplot(x=sent_lengths, ax=axs[1, 1], color='cyan')
    axs[1, 1].set_title("Sentence Length")

    # Global title
    fig.suptitle("Text Analysis Dashboard", fontsize=16)

    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    with open ("sample_text.txt", "r") as f:
        text = f.read()

    #1. Word Frequency Visualization:
    word_freq(text)

    #2. Word Length Distribution:
    word_length(text)

    #3. Character Frequency:
    char_level(text)

    #4. Sentence Length Distribution:
    sentence_length(text)

    #5. Dashboard Creation:
    create_dashboard(text)

