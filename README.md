# ATS Score Calculator

## Project Definition
The ATS Score Skill is a Python-based tool designed to analyze resumes and job descriptions, extract relevant skills, and calculate an ATS (Applicant Tracking System) score. This score helps candidates optimize their resumes for better visibility and compatibility with job requirements in ATS software commonly used by recruiters.

---

## Project Overview
The ATS Score Skill simplifies the job application process by:
- Extracting skills from resumes (PDF format) and job descriptions using the Gemini API.
- Comparing extracted skills to determine compatibility.
- Providing a user-friendly Streamlit interface for interaction.

This project is tailored for job seekers aiming to enhance their resumes and secure better job opportunities by aligning their skills with employer expectations.

---

## Key Features
- **Skill Extraction:** Leverages the Gemini API to extract skills from resumes and job descriptions.
- **Skill Comparison:** Identifies matching and missing skills between a resume and job description.
- **ATS Score Calculation:** Outputs a compatibility score based on extracted skills.
- **Streamlit Interface:** Intuitive UI with two main functionalities:
  - Skill Checker: Displays skills extracted from a resume.
  - Score Checker: Calculates the ATS score for a given job description and resume.

---

## Technical Details
- **Programming Language:** Python
- **Libraries:** Streamlit, PyPDF2, Pandas, OpenAI Gemini API
- **Dependencies:** Managed via `requirements.txt`.
- **Gemini API Usage:** The project relies on OpenAI's Gemini API for skill extraction, which requires:
  - An API key for authentication.
  - Internet connectivity to send prompts and receive responses.

---

## Project Structure
```
ATS-Score-Calculator/
|
├── skill_and_score_extraction.py  # Contains Gemini API functionality.
├── main.py                        # Streamlit interface implementation.
├── requirements.txt               # List of required Python packages.
├── README.md                      # Project documentation.
```

### **File Details:**
1. **`skill_and_score_extraction.py`:**
   - Implements functions to interact with the Gemini API.
   - Extracts skills from resumes and job descriptions.
   - Compares extracted skills to calculate an ATS score.

2. **`main.py`:**
   - Integrates `skill_and_score_extraction.py` into a Streamlit interface.
   - Provides functionality for users to upload resumes and paste job descriptions.

3. **`requirements.txt`:**
   - Contains all dependencies required to run the project.
   - Facilitates quick setup by automating package installations.
   - Example:
     ```
     streamlit
     PyPDF2
     pandas
     openai
     ```

4. **`README.md`:**
   - Comprehensive project documentation for users and contributors.

---

## Setup Instructions

### **Prerequisites:**
1. Python 3.8 or later installed on your system.
2. An OpenAI Gemini API key.

### **Steps:**
1. Clone this repository:
   ```bash
   git clone https://github.com/Parth-444/ATS-score-skill.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ATS-score-skill
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your Gemini API key:
   - Create an `.env` file in the root directory.
   - Add your API key in the following format:
     ```env
     OPENAI_API_KEY=your-api-key
     ```
5. Run the application:
   ```bash
   streamlit run main.py
   ```

---

## Gemini API Workflow
1. **Input:** Users upload their resume (PDF) and paste a job description.
2. **Processing:**
   - The resume text is extracted using PyPDF2.
   - Skills are extracted from both the resume and job description using Gemini API prompts.
   - Skill matching and ATS score calculation are performed.
3. **Output:**
   - Skills are displayed in the Skill Checker tab.
   - The ATS score is shown in the Score Checker tab.

---

## Example Usage
### **Input:**
- Resume: `Your_resume.pdf`
- Job Description: "We are seeking a Data Analyst proficient in Python, SQL, and data visualization."

### **Output:**
- Extracted Skills: `['python', 'sql', 'data visualization']`
- ATS Score: `85/100`

---

## Future Enhancements
- Add multilingual resume support.
- Improve skill extraction accuracy with advanced NLP models.
- Provide suggestions to improve ATS score.
- Include job-specific resume tailoring tips.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description.

---

**Note:** Feel free to customize this README template as per your project’s evolving needs!

