# AI Resume Optimizer

A Python Streamlit web app that leverages OpenAI GPT-3.5 to analyze, review, and suggest improvements for resumes.  
Supports **.txt**, **.docx**, and **.pdf** resume files.

---

## Features

- Upload resumes in multiple formats: `.txt`, `.docx`, `.pdf`
- Extracts clean text from uploaded files
- Uses OpenAI GPT-3.5 to provide AI-powered suggestions
- Displays AI feedback in a user-friendly web interface
- Designed for freelancers or clients who want automated resume improvement

---

## Demo

![Screenshot](screenshot-placeholder.png)  
*(Replace with an actual screenshot of your app running in Streamlit)*

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/resume-optimizer.git
cd resume-optimizer

### 2. Create a virtual environment

python3 -m venv ai-env
source ai-env/bin/activate  # Mac/Linux
# ai-env\Scripts\activate    # Windows PowerShell

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add your OpenAI API key

Create a .env file in the project root:
OPENAI_API_KEY=your_openai_api_key_here

### Usage

Run the Streamlit app:

streamlit run resume_app.py

Open your browser (Streamlit will open automatically)

Upload your resume file (.txt, .docx, or .pdf)

Click Get AI Suggestions

Review AI feedback directly in the browser

### Folder Structure
resume-optimizer/
├── resume_app.py        # Main Streamlit web app
├── resume-optimizer.py  # Original Python script (optional)
├── requirements.txt     # Python dependencies
├── .env                 # OpenAI API key (not tracked)
├── .gitignore           # Files/folders Git should ignore
└── README.md            # Project documentation

### Dependencies

Python 3.9+

Streamlit

OpenAI Python SDK (openai)

python-dotenv

python-docx

PyPDF2

Install all dependencies via:

pip install -r requirements.txt

### Notes

Uses GPT-3.5-turbo for compatibility with new OpenAI accounts

Keep .env private; do not push to GitHub

Supports multiple file formats for real-world resumes

### License

MIT License © [Jaiprakash Narayanappa]