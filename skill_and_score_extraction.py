import PyPDF2
import google.generativeai as genai
import os

key = os.getenv('genai-api')
genai.configure(api_key=key)


def extract_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text
    # with open(pdf_path, 'rb') as file:
    #     reader = PyPDF2.PdfReader(file)
    #
    #     text = ''
    #     for page_num in range(len(reader.pages)):
    #         page = reader.pages[page_num]
    #         text += page.extract_text()
    #
    # return text


def score_calculator(model, resume_text, job_description):
    prompt = """
    Imagine you are a highly intelligent and efficient hiring assistant specializing in analyzing resumes for Applicant 
    Tracking Systems (ATS). 
    Your task is to carefully analyze the resume provided below and extract relevant skills by considering:
    1. The explicit "Skills" section, if available.
    2. Skills inferred from the "Projects" and other sections, based on actions, tools, and technologies used.
    3. Analyze the classification of skills and count them as skills only if the ATS for the companies work like that.
    Be highly precise while calculating the score and while calculating score be mindful of the skills as most of the
    technical skills are used collectively for one classification of a skill.
    Calculate the ATS score on the basic of both the classification name of the skill and the technology that counts as 
    skill, be also mindful of the keywords like "real-time sentiment analysis"," "SQL," "text preprocessing," 
    "dashboard," "actionable insights," and "stakeholders," which should be present on the job description, if the resume
    equates these keywords or even more than the job description then give them high score, if there are some keywords 
    than job description then give mediocre score and if resume has no keywords related to job description then give them
    significantly lower score.  
    Then compare these extracted skills to the skills required for the following job description:
    ---
    {job_description}
    ---
    Calculate an ATS score based on the percentage match between the job description skills and the relevant skills from
     the resume. 
    Just provide these 2 as output:
    1.Skills as comma separated values
    2. The Ats score in percentage
    separate these two value in output text with the "?" symbol
    

    Resume Text:
    ---
    {resume_text}
    ---
    """
    response = model.generate_content(prompt.format(resume_text=resume_text, job_description=job_description))
    output = response.text.strip()

    extracted_skills, ats_score = output.split('?')
    skills_list = [skill.strip().lower() for skill in extracted_skills.split(',')]

    return skills_list, ats_score
