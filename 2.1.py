import streamlit as st

# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state['page'] = 'info'
if 'name' not in st.session_state:
    st.session_state['name'] = ''
if 'student_number' not in st.session_state:
    st.session_state['student_number'] = ''
if 'email' not in st.session_state:
    st.session_state['email'] = ''
if 'current_index' not in st.session_state:
    st.session_state['current_index'] = 0
if 'answers' not in st.session_state:
    st.session_state['answers'] = [None] * 10
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

# Function to reset quiz
def reset_quiz():
    st.session_state['current_index'] = 0
    st.session_state['answers'] = [None] * 10
    st.session_state['submitted'] = False
    st.session_state['page'] = 'quiz'

# Page 1: User Information
if st.session_state['page'] == 'info':
    st.title('HLTH637 Module 2 Quiz')
    st.header('Enter your details to begin')
    st.session_state['name'] = st.text_input("Name", st.session_state['name'])
    st.session_state['student_number'] = st.text_input("Student Number", st.session_state['student_number'])
    st.session_state['email'] = st.text_input("Email", st.session_state['email'])
    
    if st.button('Start Quiz'):
        if st.session_state['name'] and st.session_state['student_number'] and st.session_state['email']:
            st.session_state['page'] = 'quiz'
            st.rerun()
        else:
            st.warning("Please fill out all fields before starting the quiz.")

# Quiz questions and answers
questions = [
    {
        'text': 'What is the primary characteristic that distinguishes Big Data from traditional data in healthcare?',
        'options': ['A) Limited storage requirements', 'B) Simple formats and structures', 'C) Large volumes, high velocity, and complex variety', 'D) Minimal need for advanced analysis'],
        'correct_answer': 'C) Large volumes, high velocity, and complex variety',
        'explanation': 'Big Data is defined by its large volume, high velocity, and complex variety, which distinguish it from traditional data in healthcare.'
    },
    {
        'text': 'Which of the following is NOT one of the core Vs of Big Data?',
        'options': ['A) Volume', 'B) Validity', 'C) Velocity', 'D) Variety'],
        'correct_answer': 'B) Validity',
        'explanation': 'The core Vs of Big Data are Volume, Velocity, and Variety. Validity is not traditionally included in this list.'
    },
    {
        'text': 'Unstructured data in healthcare typically includes:',
        'options': ['A) Electronic medical records', 'B) Readings from medical devices', 'C) Diagnostic imaging and handwritten notes', 'D) Patient demographics stored in databases'],
        'correct_answer': 'C) Diagnostic imaging and handwritten notes',
        'explanation': 'Unstructured data includes complex data formats such as images, handwritten notes, and free-text data.'
    },
    {
        'text': 'Which category of data analytics focuses on predicting future outcomes using patterns from historical data?',
        'options': ['A) Descriptive Analytics', 'B) Diagnostic Analytics', 'C) Predictive Analytics', 'D) Prescriptive Analytics'],
        'correct_answer': 'C) Predictive Analytics',
        'explanation': 'Predictive Analytics uses historical data to make future predictions based on identified patterns.'
    },
    {
        'text': 'In the DIKW hierarchy, what is the significance of transforming data into wisdom?',
        'options': ['A) Storing large volumes of information', 'B) Generating actionable insights for decision-making', 'C) Reducing storage and bandwidth requirements', 'D) Ensuring ethical data usage and privacy'],
        'correct_answer': 'B) Generating actionable insights for decision-making',
        'explanation': 'Wisdom represents the highest level in the DIKW hierarchy, focusing on using insights to drive decisions.'
    }
]

# Page 2: Quiz
if st.session_state['page'] == 'quiz':
    st.title('HLTH637 Module 2 Quiz')
    
    question = questions[st.session_state['current_index']]
    st.write(question['text'])
    options = question['options']
    
    selected_option = st.radio(
        'Choose your answer:', options,
        index=options.index(st.session_state['answers'][st.session_state['current_index']]) if st.session_state['answers'][st.session_state['current_index']] in options else 0
    )
    
    if st.button('Submit Answer'):
        st.session_state['answers'][st.session_state['current_index']] = selected_option
        if st.session_state['current_index'] < len(questions) - 1:
            st.session_state['current_index'] += 1
        st.rerun()
    
    if st.button('Previous') and st.session_state['current_index'] > 0:
        st.session_state['current_index'] -= 1
        st.rerun()
    
    if st.session_state['current_index'] == len(questions) - 1 and st.button('Finish Quiz'):
        st.session_state['submitted'] = True
        st.session_state['page'] = 'results'
        st.rerun()

# Page 3: Results
if st.session_state['page'] == 'results':
    st.title('Quiz Results')
    
    correct_count = sum(1 for i, question in enumerate(questions) if st.session_state['answers'][i] == question['correct_answer'])
    total_questions = len(questions)
    
    st.write(f"Name: {st.session_state['name']}")
    st.write(f"Student Number: {st.session_state['student_number']}")
    st.write(f"Email: {st.session_state['email']}")
    st.write(f"Your Score: {correct_count}/{total_questions}")
    
    st.success("Congratulations on finishing the Emerald Group's Learning Activity!")
    
    for i, question in enumerate(questions):
        st.write(f"**Question {i+1}:** {question['text']}")
        st.write(f"Your Answer: {st.session_state['answers'][i]}")
        st.write(f"Correct Answer: {question['correct_answer']}")
        st.write(f"Explanation: {question['explanation']}")
        st.write('---')
    
    if st.button('Retake Quiz'):
        reset_quiz()
        st.rerun()
