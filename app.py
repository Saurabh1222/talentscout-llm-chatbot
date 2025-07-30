# app.py
import streamlit as st
from question_generator import generate_questions
import os
import json

st.set_page_config(page_title="TalentScout AI", page_icon="🤖")
st.title("🤖 TalentScout Hiring Assistant")
# Place this at the top of your Streamlit app (just below the title)
exit_input = st.text_input("Type 'exit' or 'bye' to end the chat early (optional):")

if exit_input.lower() in ["exit", "quit", "bye"]:
    st.warning("👋 Conversation ended by the user.")
    st.stop()  # Ends the Streamlit script here
    
# Step 1: Candidate Info Collection
st.subheader("📝 Candidate Information")
name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
experience = st.number_input("Years of Experience", min_value=0)
location = st.text_input("Current Location")
desired_position = st.text_input("Desired Position")

# Save candidate info to session
if st.button("Next ➡️"):
    if all([name, email, phone, location, desired_position]):
        st.session_state["info_collected"] = True
        st.session_state["candidate_info"] = {
            "name": name,
            "email": email,
            "phone": phone,
            "experience": experience,
            "location": location,
            "desired_position": desired_position
        }
        st.success("✅ Info saved! Now enter your tech stack.")
    else:
        st.warning("Please fill all the fields.")

# Step 2: Tech Stack Input
if st.session_state.get("info_collected"):
    st.subheader("💻 Your Tech Stack")
    tech_input = st.text_input("List your skills separated by commas (e.g. Python, Django, React)")
    
    if st.button("Generate Questions"):
        if tech_input:
            tech_list = [tech.strip() for tech in tech_input.split(",")]
            with st.spinner("Generating technical questions using Gemini..."):
                questions = generate_questions(tech_list)
            st.session_state["questions"] = questions  # ✅ Store in session
            st.session_state["tech_list"] = tech_list  # ✅ Also store tech list
        else:
            st.warning("Please enter at least one tech skill.")

# Step 3: Store Answers
if "questions" in st.session_state:
    st.subheader("🧠 Technical Questions:")

    candidate_answers = []
    for item in st.session_state["questions"]:
        for tech, qns in item.items():
            st.markdown(f"### 💻 {tech}")
            st.write(qns)
            ans = st.text_area(f"✍️ Your answer for {tech}:", key=tech)
            # Fallback if blank
            if ans.strip() == "":
                st.warning(f"⚠️ You left the answer for **{tech}** empty. You can still submit.")
            candidate_answers.append({
                tech: {
                    "question": qns,
                    "answer": ans
                }
            })

    if st.button("✅ Submit All Answers"):
        # Final output dictionary
        output = {
            "candidate_info": st.session_state["candidate_info"],
            "tech_stack_responses": candidate_answers
        }

        # Create data directory if not present
        os.makedirs("data", exist_ok=True)

        # Save using email as unique identifier
        filename = f"data/{st.session_state['candidate_info']['email'].replace('@', '_at_')}.json"
        with open(filename, "w") as f:
            json.dump(output, f, indent=2)

        st.success(f"Thanks {st.session_state['candidate_info']['name']} for your time!")
        st.markdown("✅ Your responses have been recorded.")
        st.markdown("📩 Our team will reach out to you for the next steps.")
