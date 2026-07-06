import re

JOB_TITLES = [
    "software engineer",
    "software developer",
    "python developer",
    "web developer",
    "data analyst",
    "data scientist",
    "machine learning engineer",
    "ai engineer",
    "intern",
    "project trainee"
]


def extract_experience(text):

    text = text.lower()

    experience = []

    # Find years of experience
    year_pattern = r"\d+\+?\s*(?:years?|yrs?)"

    years = re.findall(year_pattern, text)

    experience.extend(years)

    # Find job titles
    for title in JOB_TITLES:

        if title in text:
            experience.append(title.title())

    return sorted(set(experience))