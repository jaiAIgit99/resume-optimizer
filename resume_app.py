# resume_app.py
import os
import streamlit as st
from dotenv import load_dotenv
import openai

# For .docx files
from docx import Document

# For PDF files
import PyPDF2

# --- Step 1: Load API Key ---
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# --- Step 2: Streamlit UI ---
st.title("AI Resume Optimizer")
st.write("Upload your resume (.txt, .docx, .pdf) and get AI improvement suggestions!")

uploaded_file = st.file_uploader(
    "Choose your resume file", type=["txt", "docx", "pdf"]
)

def read_docx(file):
    """Extract text from Word (.docx) file"""
    doc = Document(file)
    full_text = [para.text for para in doc.paragraphs]
    return "\n".join(full_text)

def read_pdf(file):
    """Extract text from PDF file"""
    reader = PyPDF2.PdfReader(file)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
    return full_text

# --- Step 3: Process uploaded file ---
if uploaded_file is not None:
    file_name = uploaded_file.name
    if file_name.endswith(".txt"):
        resume_text = uploaded_file.read().decode("utf-8")
    elif file_name.endswith(".docx"):
        resume_text = read_docx(uploaded_file)
    elif file_name.endswith(".pdf"):
        resume_text = read_pdf(uploaded_file)
    else:
        st.error("Unsupported file format")
        resume_text = None

    if resume_text:
        st.subheader("Resume Content")
        st.text_area("Here is your resume text:", resume_text, height=200)

        # --- Step 4: Send to OpenAI ---
        if st.button("Get AI Suggestions"):
            with st.spinner("Analyzing resume..."):
                try:
                    response = openai.chat.completions.create(
                        model="gpt-3.5-turbo",  # safe for new accounts
                        messages=[
                            {"role": "system", "content": "You are an expert career coach."},
                            {"role": "user", "content": f"Review this resume and suggest improvements:\n{resume_text}"}
                        ],
                        temperature=0.7
                    )
                    suggestions = response.choices[0].message.content
                    st.subheader("AI Suggestions")
                    st.write(suggestions)
                except Exception as e:
                    st.error(f"Error: {e}")