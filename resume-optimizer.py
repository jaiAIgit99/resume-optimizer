# resume-optimizer.py (for openai>=1.0)

import os
from dotenv import load_dotenv
import openai

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

resume_text = """
John Doe
Software Engineer with 3 years of experience in Python and JavaScript.
Worked on web applications, APIs, and data pipelines.
Education: B.Tech in Computer Science
Skills: Python, JavaScript, Git, SQL
"""

try:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert career coach."},
            {"role": "user", "content": f"Review this resume and suggest improvements:\n{resume_text}"}
        ],
        temperature=0.7
    )

    print("AI Suggestions:\n")
    print(response.choices[0].message.content)

except Exception as e:
    print("Error:", e)