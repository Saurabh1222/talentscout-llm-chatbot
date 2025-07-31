# question_generator.py
import google.generativeai as genai
import os

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_questions(tech_stack):
    questions = []
    for tech in tech_stack:
        prompt = f"Generate 3 technical interview questions for a candidate skilled in {tech}. The questions must be one line to reduce complexity."
        response = model.generate_content(prompt)
        questions.append({tech: response.text})
    return questions
