import re


def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_phone(text):
    pattern = r"\+?\d[\d\s\-]{8,}\d"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_linkedin(text):
    pattern = r"(https?://)?(www\.)?linkedin\.com/[^\s]+"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_github(text):
    pattern = r"(https?://)?(www\.)?github\.com/[^\s]+"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"