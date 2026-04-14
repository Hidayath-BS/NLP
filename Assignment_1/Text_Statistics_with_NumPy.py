import re 
import numpy as np
from collections import Counter

def word_freq(text):
    """
    create a word frequency dictionary
    """
    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = Counter(words)

    print(f"Word Frequency:\n{word_freq}")

    frequency_arr = np.array(list(word_freq.values()))
    print(f"Word Frequency Array:\n{frequency_arr}")

    mean_freq = np.mean(frequency_arr)
    median_freq = np.median(frequency_arr)
    standard_freq = np.std(frequency_arr)

    print(f"Mean Frequency: {mean_freq}, Median Frequency: {median_freq}, Standard Deviation: {standard_freq}")

    p25_freq = np.percentile(frequency_arr, 25)
    p50_freq = np.percentile(frequency_arr, 50)
    p75_freq = np.percentile(frequency_arr, 75)

    print(f"25th Percentile: {p25_freq}, 50th Percentile: {p50_freq}, 75th Percentile: {p75_freq}")

def char_level(text):
    """
    character level analysis
    """
    text = re.sub(r'\s+','', text)
    char_freq = Counter(text)

    print(f"Character Frequency:\n{char_freq}")

    most_common_char = char_freq.most_common(1)
    least_common_char = char_freq.most_common()[-1]
    print(f"Most Common Character: {most_common_char}, Least Common Character: {least_common_char}")

    vowels = set('aeiou')
    vowel_count = sum(char_freq[char] for char in vowels)
    constant_count = sum(char_freq[char] for char in char_freq if char not in vowels)
    ratio = vowel_count / constant_count if constant_count > 0 else 0

    print(f"Vowel Count: {vowel_count}, Consonant Count: {constant_count}")
    print(f"Vowel to Consonant Ratio: {ratio}")

def sentence_length(text):
    """
    sentence length analysis
    """
    sentences = re.split(r'[.!?]+', text)
    sentence_lengths = [len(sentence.split()) for sentence in sentences if sentence.strip()]

    print(f"Sentence Lengths: {sentence_lengths}")

    mean_length = np.mean(sentence_lengths)
    max_length = np.max(sentence_lengths)

    print(f"Mean Sentence Length: {mean_length}, Maximum Sentence Length: {max_length}")

if __name__ == "__main__":
    with open ("sample_text.txt", "r") as f:
        text = f.read()

    #1. word frequency analysis
    word_freq(text)

    #2. charecter level analysis
    char_level(text)

    #3. sentence length analysis
    sentence_length(text)