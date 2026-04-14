import re
import pandas as pd

def load_data(file_path):
    """
    Load the dataset from the given file path.
    handling with encoding issues by specifying 'utf-8'.
    """

    #2. Handle different encodings
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def basic_statistics(text):
    """
    Calculate and return basic statistics about the text data.
    """
    num_characters = len(text)
    num_words = len(text.split())
    num_sentences = len(re.split(r'[.!?]+', text)) - 1
    avg_word = num_characters / num_words
    avg_sentence = num_words / num_sentences

    print(f"num_characters: {num_characters}, num_words: {num_words}, num_sentences: {num_sentences}")
    print(f"avg_word_length: {avg_word}, avg_sentence_length: {avg_sentence}")

def create_dataframe(text, file_name):
    """
    Create a Pandas DataFrame with document metadata.
    """
    data = {
        'document_id': 1,
        'file_name': file_name,
        'num_words': len(text.split()),
        'num_characters': len(text),
    }
    df = pd.DataFrame([data])

    print(f"DataFrame:\n{df}")
    return df

if __name__ == "__main__":

    file_name = "alice_in_wonderland.txt"

    #1. Load text data from files using Python file I/O
    text_data = load_data(file_name)

    #3. Display basic statistics:
    basic_statistics(text_data)

    #4. Create a Pandas DataFrame with document metadata
    df = create_dataframe(text_data, file_name)

    #5. Export statistics to CSV file
    df.to_csv('document_statistics.csv', index=False)
    
