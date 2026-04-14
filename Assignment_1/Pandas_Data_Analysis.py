import re
import pandas as pd
from collections import Counter

def create_df(text):
    """
    Create a DataFrame with word frequencies
    """
    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = Counter(words)

    vowels = set('aeiou')

    df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])
    df['length'] = df['Word'].apply(len)
    df['first_letter'] = df['Word'].str[0]
    df['vowel_count'] = df['Word'].apply(lambda x: sum(1 for char in x if char in vowels))

    df.set_index('Word', inplace=True)
    
    print(df.head())
    return df

def perform_group_by(df):
    """
    Perform group by operation
    """
    group_by_length = df.groupby('length')['Frequency'].sum()
    print(f"Group by Length:\n{group_by_length}")

    group_by_first_letter = df.groupby('first_letter')['Frequency'].sum()
    print(f"Group by First Letter:\n{group_by_first_letter}")
    

def sort_df(df):
    """
    Sort and filter the DataFrame
    """
    sorted_df = df.sort_values(by='Frequency', ascending=False).head(50)
    print(f"Sorted 50 DataFrame:\n{sorted_df}")

    long_word = df[df["length"] > 10]
    print(f"Words with length greater than 10:\n{long_word}")

def pivot_table(df):
    """
    Create a pivot table
    """
    pivot = df.pivot_table(values='Frequency', index='first_letter', columns='length', aggfunc='sum', fill_value=0)
    print(f"Pivot Table:\n{pivot}")

    crosstab = pd.crosstab(df['length'], df['first_letter'])
    print("crosstab:",crosstab)

if __name__ == "__main__":
    with open ("sample_text.txt", "r") as f:
        text = f.read()

    #1. create a DataFrame with word frequencies
    df =create_df(text)

    #2. perform group by operation
    perform_group_by(df)

    #3. Sort and filter the DataFrame
    sort_df(df)

    #4. create a pivot table
    pivot_table(df)