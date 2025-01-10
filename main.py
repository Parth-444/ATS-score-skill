from skill_and_score_extraction import *
import streamlit as st

st.title('ATS analyser')
page = st.sidebar.radio("Go to", ["Score Checker", "Skill Checker"])
model = genai.GenerativeModel("gemini-1.5-flash")
if page == "Score Checker":
    # Score Checker Page
    st.header("ATS Score Checker")
    st.subheader("Upload Your Resume")
    uploaded_file = st.file_uploader("Browse and upload your resume (PDF format)", type=["pdf"])
    st.subheader("Paste Job Description")
    job_description = st.text_area("Paste the job description here:")
    if st.button("Check ATS Score"):
        if uploaded_file and job_description:
            # Placeholder for output (to be replaced with backend function call)
            r_text = extract_text(uploaded_file)
            score = score_calculator(model, r_text, job_description)[1]
            ats_score = score  # Example score
            st.success(f"Your ATS Score is: {ats_score}")
        else:
            st.error("Please upload a resume and paste the job description.")
elif page == "Skill Checker":
    # Skill Checker Page
    st.header("Skill Checker")

    # Resume Upload
    # st.subheader("Upload Your Resume")
    uploaded_file = st.file_uploader("Browse and upload your resume (PDF format)", type=["pdf"],
                                         key="skill_checker")
    if st.button("Extract Skills"):
        if uploaded_file:
            # Placeholder for output (to be replaced with backend function call)
            r_text = extract_text(uploaded_file)
            skills = score_calculator(model, r_text,'')[0]
            extracted_skills = skills
            extracted_skills= [skill.title() for skill in extracted_skills]
            st.success("Skills Found in Your Resume:")
            st.write(", ".join(extracted_skills))
        else:
            st.error("Please upload a resume.")







