import re

def clean_text(text):
    """
    Cleans resume text by:
    - converting to lowercase
    - removing special characters
    - removing extra spaces
    """

    # Convert to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()