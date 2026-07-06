import streamlit as st
import plotly.graph_objects as go

from utils.pdf_parser import extract_text
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills


from utils.contact_extractor import (
    extract_email,
    extract_phone,
    extract_linkedin,
    extract_github
)

from utils.education_extractor import extract_education
from utils.experience_extractor import extract_experience
from utils.ats_score import calculate_ats_score


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and compare it with a job description.")

# -----------------------------
# Upload Resume
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

# -----------------------------
# Job Description
# -----------------------------
job_description = st.text_area(
    "Paste Job Description",
    height=220
)

# -----------------------------
# Main Logic
# -----------------------------
if uploaded_file:

    # Save uploaded PDF temporarily
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Extract Resume Text
    resume_text = extract_text("temp_resume.pdf")

    # Clean Resume Text
    cleaned_text = clean_text(resume_text)

    # Extract Information
    skills = extract_skills(cleaned_text)

    education = extract_education(cleaned_text)

    experience = extract_experience(cleaned_text)

    email = extract_email(resume_text)
    phone = extract_phone(resume_text)
    linkedin = extract_linkedin(resume_text)
    github = extract_github(resume_text)

    # Default Values
    ats_score = 0
    matched_skills = []
    missing_skills = []
    jd_skills = []

    # -----------------------------
    # Calculate ATS
    # -----------------------------
    if job_description.strip():

        cleaned_jd = clean_text(job_description)

        jd_skills = extract_skills(cleaned_jd)

        ats_score, matched_skills, missing_skills = calculate_ats_score(
            cleaned_text,
            cleaned_jd,
            skills,
            jd_skills,
            education,
            experience
        )

    # ====================================================
    # DASHBOARD
    # ====================================================

    st.divider()

    st.header("📊 Resume Analysis Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ATS Score", f"{ats_score}%")

    with col2:
        st.metric("Skills Found", len(skills))

    with col3:
        st.metric("Missing Skills", len(missing_skills))

    st.progress(min(int(ats_score), 100))
    fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=ats_score,
    title={"text": "ATS Score"},
    gauge={
        "axis": {"range": [0, 100]},
        "bar": {"color": "green"},
        "steps": [
            {"range": [0, 50], "color": "#ffcccc"},
            {"range": [50, 75], "color": "#ffe680"},
            {"range": [75, 100], "color": "#ccffcc"}
        ]
    }
))

    st.plotly_chart(fig, use_container_width=True)

    # ATS Feedback

    if ats_score >= 90:
        st.success("🎉 Excellent! Your resume is highly matched with the job.")

    elif ats_score >= 75:
        st.info("👍 Good match. Add the missing skills to improve further.")

    elif ats_score >= 60:
        st.warning("⚠ Moderate match. Improve your resume before applying.")

    else:
        st.error("❌ Low match. Your resume is missing important requirements.")

    st.divider()

    # ====================================================
    # EDUCATION & EXPERIENCE
    # ====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🎓 Education")

        if education:
            for edu in education:
                st.success(edu)
        else:
            st.warning("Education not found.")

    with col2:

        st.subheader("💼 Experience")

        if experience:
            for exp in experience:
                st.success(exp)
        else:
            st.warning("Experience not found.")

    st.divider()

    # ====================================================
    # SKILLS
    # ====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🛠 Resume Skills")

        if skills:
            for skill in skills:
                st.success(skill.title())

        else:
            st.warning("No skills detected.")

    with col2:

        st.subheader("❌ Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.error(skill.title())
        else:
            st.success("No Missing Skills 🎉")

    st.divider()

    # ====================================================
    # MATCHED SKILLS
    # ====================================================

    st.subheader("✅ Matching Skills")

    if matched_skills:
        cols = st.columns(3)

        for i, skill in enumerate(matched_skills):
            cols[i % 3].success(skill.title())

    else:
        st.warning("No matching skills found.")

    st.divider()

    # ====================================================
    # CONTACT INFORMATION
    # ====================================================

        # ====================================================
    # RESUME SUGGESTIONS
    # ====================================================

    st.subheader("💡 Resume Suggestions")

    if missing_skills:

        st.warning("Consider adding these skills:")

        for skill in missing_skills:
            st.write("✔", skill.title())

    else:

        st.success("🎉 Excellent! Your resume already contains all required skills.")

    st.divider()

    # ====================================================
    # DOWNLOAD REPORT
    # ====================================================

    

    # ====================================================
    # RESUME TEXT
    # ====================================================

    with st.expander("📄 View Original Resume Text"):
        st.text(resume_text)

    with st.expander("🧹 View Cleaned Resume Text"):
        st.write(cleaned_text)

else:
    st.info("👆 Upload a resume PDF to begin analysis.")