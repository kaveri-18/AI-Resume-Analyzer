from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_ats_score(
    resume_text,
    jd_text,
    resume_skills,
    jd_skills,
    education,
    experience
):

    # Cosine similarity
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors)[0][1] * 100

    # Skill matching
    resume_set = set(skill.lower() for skill in resume_skills)
    jd_set = set(skill.lower() for skill in jd_skills)

    matched_skills = sorted(resume_set & jd_set)
    missing_skills = sorted(jd_set - resume_set)

    if len(jd_set) == 0:
        skill_score = 100
    else:
        skill_score = (len(matched_skills) / len(jd_set)) * 100

    education_score = 100 if education else 0
    experience_score = 100 if experience else 0

    final_score = (
        0.70 * skill_score +
        0.10 * similarity +
        0.10 * education_score +
        0.10 * experience_score
    )

    return round(final_score, 2), matched_skills, missing_skills