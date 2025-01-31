import streamlit as st
import random

# Define questions with explanations
questions = [
    {
        "question": "What is the primary characteristic that distinguishes Big Data from traditional data in healthcare?",
        "options": ["Limited storage requirements", "Simple formats and structures", "Large volumes, high velocity, and complex variety", "Minimal need for advanced analysis"],
        "answer": "Large volumes, high velocity, and complex variety",
        "explanation": "Big Data in healthcare is defined by its large volume, high velocity (speed of data processing), and complex variety (structured and unstructured data)."
    },
    {
        "question": "Which of the following is NOT one of the core Vs of Big Data as mentioned in the document?",
        "options": ["Volume", "Validity", "Velocity", "Variety"],
        "answer": "Validity",
        "explanation": "The core Vs of Big Data are Volume, Velocity, and Variety. Validity is important, but it is not one of the core Vs."
    }
]

# Shuffle questions
random.shuffle(questions)

# Streamlit app
st.title("HLTH637 Quiz Bot")
st.write("Test your knowledge on health informatics and big data!")

# Session state to track progress
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.submitted = False

# Get current question
if st.session_state.question_index < len(questions):
    current_q = questions[st.session_state.question_index]
    st.subheader(current_q["question"])
    
    user_answer = st.radio("Select your answer:", current_q["options"], index=None, key=f"question_{st.session_state.question_index}")
    
    if st.button("Submit Answer"):
        if user_answer:
            st.session_state.submitted = True
            if user_answer == current_q["answer"]:
                st.success("Correct! ✅")
                st.session_state.score += 1
            else:
                st.error(f"Wrong ❌ The correct answer is: {current_q['answer']}")
                st.write(f"**Explanation:** {current_q['explanation']}")
            
    if st.session_state.submitted and st.button("Next Question"):
        st.session_state.question_index += 1
        st.session_state.submitted = False
        st.experimental_rerun()
else:
    st.write("## Quiz Complete! 🎉")
    st.write(f"Your final score: {st.session_state.score}/{len(questions)}")
    if st.button("Restart Quiz"):
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.submitted = False
        st.experimental_rerun()

# Run this script with: `streamlit run your_script.py`
