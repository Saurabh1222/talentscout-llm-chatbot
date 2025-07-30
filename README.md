# 🤖 TalentScout: LLM-Based Hiring Assistant Chatbot

TalentScout is a smart hiring assistant chatbot built with **Streamlit** and **Gemini Pro (Google AI)**.  
It helps simulate the first round of candidate screening by collecting their details and asking tech-specific questions based on their declared stack.

---

## 🚀 Features

- 📋 Collects candidate info (name, email, experience, etc.)
- 💻 Accepts tech stack input
- 🧠 Uses **Gemini Pro** to generate 3 relevant questions per tech skill
- 📝 Lets candidates type answers for each generated question
- 💾 Saves questions + answers + candidate info into a local `.json` file
- 🔁 Allows re-generation of questions if needed
- 🔐 Secures API key using a `.env` file
- 🛡️ Handles reruns with `st.session_state` to preserve context
- 👋 Supports graceful exit using keywords like `exit`, `bye`, etc.

---

## 🛠 Tech Stack

| Component | Tool |
|----------|------|
| Frontend | Streamlit |
| LLM      | Gemini Pro (Google Generative AI) |
| Backend  | Python |
| Env Mgmt | python-dotenv |
| Storage  | Local JSON file |

---

## 🧠 Prompt Strategy

Each skill is processed with a prompt like:

> “Generate 3 technical interview questions for a candidate skilled in Python.”

The result from Gemini is stored alongside the candidate’s typed answers.

---

## 📂 Project Structure

talentscout_llm_chatbot/
├── app.py # Streamlit frontend
├── question_generator.py # LLM integration
├── .env # API key (ignored in Git)
├── requirements.txt
├── data/ # Folder where JSON files are saved
└── README.md

## ⚙️ Challenges & Solutions

| Challenge                               | Solution                                      |
| --------------------------------------- | --------------------------------------------- |
| Avoiding hardcoded API keys             | Used `.env` and `python-dotenv`               |
| Preserving multi-step conversation flow | Used `st.session_state`                       |
| Handling Gemini’s response format       | Extracted `.text` and cleaned question string |
| Avoiding unnecessary re-generation      | Cached responses using session                |
| Handling unexpected input or exits      | Added `exit` command handling & fallbacks     |


## 🙌 Acknowledgements

- Streamlit
- Google Gemini Pro API
- python-dotenv
- Prompt Engineering Guide