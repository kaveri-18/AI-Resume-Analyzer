import re

EDUCATION_KEYWORDS = [
    "bachelor of technology",
    "b.tech",
    "b.e",
    "be",
    "master of technology",
    "m.tech",
    "m.e",
    "mba",
    "bca",
    "mca",
    "b.sc",
    "m.sc",
    "phd",
    "diploma"
]


def extract_education(text):

    text = text.lower()

    education = []

    for keyword in EDUCATION_KEYWORDS:

        if keyword in text:
            education.append(keyword.upper())

    return sorted(set(education))