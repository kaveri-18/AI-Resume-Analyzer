import re

# List of common technical skills
SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "pandas",
    "numpy",
    "tensorflow",
    "keras",
    "opencv",
    "scikit-learn",
    "aws",
    "azure",
    "docker",
    "kubernetes",
    "git",
    "github",
    "excel",
    "power bi",
    "tableau",
    "mongodb",
    "flask",
    "streamlit"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(set(found_skills))