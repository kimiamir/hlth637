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
        'explanation': 'Big Data is defined by its large volume, high velocity, and complex variety, which distinguish it from traditional data in healthcare.',
        'wrong_explanations': {
            'A) Limited storage requirements': 'Big Data requires extensive storage solutions, unlike traditional data.',
            'B) Simple formats and structures': 'Big Data often consists of unstructured and complex formats.',
            'D) Minimal need for advanced analysis': 'Big Data requires advanced analytical tools and techniques.'
        }
    },
    {
        'text': 'Which of the following is NOT one of the core Vs of Big Data?',
        'options': ['A) Volume', 'B) Validity', 'C) Velocity', 'D) Variety'],
        'correct_answer': 'B) Validity',
        'explanation': 'The core Vs of Big Data are Volume, Velocity, and Variety. Validity is not traditionally included in this list.',
        'wrong_explanations': {
            'A) Volume': 'Volume refers to the massive amount of data generated.',
            'C) Velocity': 'Velocity describes the speed at which data is generated and processed.',
            'D) Variety': 'Variety indicates the different types of data formats (structured, semi-structured, unstructured).'
        }
    },
    {
        'text': 'Unstructured data in healthcare typically includes:',
        'options': ['A) Electronic medical records', 'B) Readings from medical devices', 'C) Diagnostic imaging and handwritten notes', 'D) Patient demographics stored in databases'],
        'correct_answer': 'C) Diagnostic imaging and handwritten notes',
        'explanation': 'Unstructured data includes complex data formats such as images, handwritten notes, and free-text data.',
        'wrong_explanations': {
            'A) Electronic medical records': 'These are structured data as they are stored in databases.',
            'B) Readings from medical devices': 'These are semi-structured data rather than unstructured.',
            'D) Patient demographics stored in databases': 'These are structured data, organized in predefined formats.'
        }
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
    },
    {
        'text': 'Artificial Intelligence (AI) in public health is used to:',
        'options': ['A) Store and transfer large data volumes', 'B) Mimic human intelligence to support health services', 'C) Replace healthcare workers in hospitals', 'D) Remove inconsistencies in structured data'],
        'correct_answer': 'B) Mimic human intelligence to support health services',
        'explanation': 'AI in public health is used to support healthcare services by mimicking human intelligence in decision-making.'
    },
    {
        'text': 'Which of the following challenges is associated with Big Data privacy risks in healthcare?',
        'options': ['A) Lack of sufficient data for analysis', 'B) Inability to access medical devices', 'C) Potential re-identification of anonymous data', 'D) Reduced accuracy of health information'],
        'correct_answer': 'C) Potential re-identification of anonymous data',
        'explanation': 'One major privacy concern in Big Data is the risk of re-identifying individuals from anonymized data.'
    },
    {
        'text': 'What mitigation strategy is suggested to address data storage challenges in Big Data applications?',
        'options': ['A) Centralizing all data in physical servers', 'B) Storing unstructured data in manual records', 'C) Using cloud computing with enhanced privacy measures', 'D) Eliminating unstructured data from analysis'],
        'correct_answer': 'C) Using cloud computing with enhanced privacy measures',
        'explanation': 'Cloud computing provides scalable storage solutions and enhanced privacy mechanisms for handling large datasets.'
    },
    {
        'text': 'During the COVID-19 pandemic, what was a major issue affecting Big Data processing and analysis?',
        'options': ['A) Lack of structured data', 'B) Delays caused by inconsistent reporting standards', 'C) Over-reliance on manual reporting', 'D) Too many predictive models being applied'],
        'correct_answer': 'B) Delays caused by inconsistent reporting standards',
        'explanation': 'Inconsistent reporting standards during COVID-19 led to data delays, affecting timely analysis and decision-making.'
    },
    {
        'text': 'How do business intelligence tools like Power BI enhance data analysis in public health?',
        'options': ['A) They automate clinical diagnoses', 'B) They reduce the need for trained personnel', 'C) They provide data visualization and transformation capabilities', 'D) They secure patient records against unauthorized access'],
        'correct_answer': 'C) They provide data visualization and transformation capabilities',
        'explanation': 'Business intelligence tools like Power BI help analyze and visualize data, making insights more accessible.'
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
    
    st.success("Congratulations on finishing the Emerald Group's Module 2 Learning Activity! Please take a screenshot and send this to our TA")
    
    for i, question in enumerate(questions):
        st.write(f"**Question {i+1}:** {question['text']}")
        st.write(f"Your Answer: {st.session_state['answers'][i]}")
        st.write(f"Correct Answer: {question['correct_answer']}")
        st.write(f"Explanation: {question['explanation']}")
        st.write('---')
    
    if st.button('Retake Quiz'):
        reset_quiz()
        st.rerun()
