import streamlit as st

# Define quiz questions
questions = [
    {
        "question": "During the COVID-19 pandemic, what was a major issue affecting Big Data processing and analysis?",
        "options": ["A) Lack of structured data", "B) Delays caused by inconsistent reporting standards", "C) Over-reliance on manual reporting", "D) Too many predictive models being applied"],
        "answer": "B) Delays caused by inconsistent reporting standards",
        "explanation": "During COVID-19, inconsistent reporting standards across regions caused significant delays in Big Data processing and analysis."
    },
    {
        "question": "How do business intelligence tools like Power BI enhance data analysis in public health?",
        "options": ["A) They automate clinical diagnoses", "B) They reduce the need for trained personnel", "C) They provide data visualization and transformation capabilities", "D) They secure patient records against unauthorized access"],
        "answer": "C) They provide data visualization and transformation capabilities",
        "explanation": "Power BI and similar tools enhance public health data analysis by enabling data visualization and transformation, making insights more accessible and actionable."
    }
]

# Initialize session state variables
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.submitted = False
    st.session_state.user_answer = None

# Get the current question
if st.session_state.question_index < len(questions):
    current_q = questions[st.session_state.question_index]
    st.title("HLTH637 Quiz Bot")
    st.write("Test your knowledge on health informatics and big data!")
    
    st.subheader(current_q["question"])
    
    if not st.session_state.submitted:
        user_answer = st.radio("Select your answer:", current_q["options"], index=None, key=f"q_{st.session_state.question_index}")
        if st.button("Submit Answer"):
            if user_answer is None:
                st.warning("Please select an answer before submitting.")
            else:
                st.session_state.submitted = True
                st.session_state.user_answer = user_answer
                if user_answer == current_q["answer"]:
                    st.success("Correct! ✅")
                    st.session_state.score += 1
                else:
                    st.error(f"Wrong ❌ The correct answer is: {current_q['answer']}")
                st.write(f"**Explanation:** {current_q['explanation']}")
    
    if st.session_state.submitted:
        if st.session_state.question_index < len(questions) - 1:
            if st.button("Next Question"):
                st.session_state.question_index += 1
                st.session_state.submitted = False
                st.session_state.user_answer = None
                st.experimental_rerun()
        else:
            st.write("## Quiz Complete! 🎉")
            st.write(f"Your final score: {st.session_state.score}/{len(questions)}")
            if st.button("Restart Quiz"):
                st.session_state.question_index = 0
                st.session_state.score = 0
                st.session_state.submitted = False
                st.session_state.user_answer = None
                st.rerun()

# Run this script with: `streamlit run your_script.py`
