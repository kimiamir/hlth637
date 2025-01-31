import streamlit as st

# Title
st.title('HLTH637 Quiz')

# Quiz questions and answers
questions = [
    {
        'text': 'What is the primary characteristic that distinguishes Big Data from traditional data in healthcare?',
        'options': ['A) Limited storage requirements', 'B) Simple formats and structures', 'C) Large volumes, high velocity, and complex variety', 'D) Minimal need for advanced analysis'],
        'correct_answer': 'C) Large volumes, high velocity, and complex variety',
        'explanation': 'Big Data is defined by its large volume, high velocity, and complex variety, which distinguish it from traditional data in healthcare.'
    },
    {
        'text': 'Which of the following is NOT one of the core Vs of Big Data as mentioned in the document?',
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

current_index = st.session_state.get('current_index', 0)

if 'answers' not in st.session_state or len(st.session_state['answers']) != len(questions):
    st.session_state['answers'] = [None] * len(questions)

if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

if current_index < len(questions):
    question = questions[current_index]
    st.write(question['text'])

    options = question['options']
    selected_option = st.radio(
        'Choose your answer:',
        options,
        index=options.index(st.session_state['answers'][current_index]) if st.session_state['answers'][current_index] in options else 0
    )

    if st.button('Submit Answer'):
        st.session_state['answers'][current_index] = selected_option
        if current_index < len(questions) - 1:
            st.session_state['current_index'] += 1

    if st.button('Previous') and current_index > 0:
        st.session_state['current_index'] -= 1

else:
    st.session_state['submitted'] = True

if st.session_state['submitted']:
    st.write('Quiz Completed!')
    st.write('Review your answers below:')

    for i, question in enumerate(questions):
        st.write(f"**Question {i+1}:** {question['text']}")
        st.write(f"Your Answer: {st.session_state['answers'][i]}")
        st.write(f"Correct Answer: {question['correct_answer']}")
        st.write(f"Explanation: {question['explanation']}")
        st.write('---')

st.session_state['current_index'] = current_index
