import re

def load_data(file_path):
    """
    Load the dataset from the given file path.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def extract_email_addresses(text):
    """
    Extract email addresses from the given text.
    """
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_addresses = re.findall(email_pattern, text)
    count_occurrences = len(email_addresses)
    unque_emails = set(email_addresses)

    print(f"Total occurrences of email addresses: {count_occurrences}")
    print(f"Unique email addresses: {unque_emails}")

def extract_phone_numbers(text):
    """
    Extract phone numbers from the given text.
    """
    phone_pattern = r'(\+1-\d{3}-\d{3}-\d{4}|\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4})'
    phone_numbers = re.findall(phone_pattern, text)

    print(f"Phone numbers found: {phone_numbers}")

    normalized_numbers = []
    for number in phone_numbers:
        normalized = re.sub(r'\D', '', number)
        normalized = normalized[1:4] + '-' + normalized[4:7] + '-' + normalized[7:]
        normalized_numbers.append(normalized)

    print(f"Normalized phone numbers: {normalized_numbers}")

def extract_hashtags_and_mentions(text):
    """
    Extract hashtags and mentions from the given text.
    """
    hashtag_pattern = r'#\w+'
    mention_pattern = r'@\w+'
    hashtags = re.findall(hashtag_pattern, text)
    mentions = re.findall(mention_pattern, text)

    print(f"Hashtags found: {hashtags}")
    print(f"Mentions found: {mentions}")
    
def extract_urls(text):
    """
    Extract URLs from the given text.
    """
    url_pattern = r'https?://[^\s]+'
    urls = re.findall(url_pattern, text)


    print(f"URLs found: {urls}")

def extract_custom_pattern(text):
    """
    Extract custom patterns from the given text.
    """
    date_pattern = r'\b(\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})\b'
    dates = re.findall(date_pattern, text)

    print(f"Dates found: {dates}")

    currency_pattern = r'[$£€]\d+(?:\.\d{2})?'
    currencies = re.findall(currency_pattern, text)

    print(f"Currency amounts found: {currencies}")

if __name__ == "__main__":

    file_name = "sample_text.txt"

    # Load text data from files.
    text_data = load_data(file_name)

    #1. Extract email addresses.
    extract_email_addresses(text_data)

    #2. Extract phone numbers.
    extract_phone_numbers(text_data)

    #3. hastags and mentions extraction.
    extract_hashtags_and_mentions(text_data)

    #4. URL extraction.
    extract_urls(text_data)

    #5. custom pattern extraction.
    extract_custom_pattern(text_data)
