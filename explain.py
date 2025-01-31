import streamlit as st

# Title
st.title('HLTH637 Quiz')

# Quiz questions and answers
questions = [
    {
        'text': 'What is the primary characteristic that distinguishes Big Data from traditional data in healthcare?',
        'options': ['A) Limited storage requirements', 'B) Simple formats and structures', 'C) Large volumes, high velocity, and complex variety', 'D) Minimal need for advanced analysis'],
        'correct_answer': 'C) Large volumes, high velocity, and complex variety',
        'detailed_explanation': {
            'A) Limited storage requirements': 'Big Data requires substantial storage, whereas traditional data often has smaller storage needs.',
            'B) Simple formats and structures': 'Big Data includes unstructured, semi-structured, and structured data, making it complex.',
            'C) Large volumes, high velocity, and complex variety': 'Correct! These three characteristics define Big Data, distinguishing it from traditional data.',
            'D) Minimal need for advanced analysis': 'Big Data necessitates advanced analytics, machine learning, and AI for meaningful insights.'
        }
    },
    {
        'text': 'Which of the following is NOT one of the core Vs of Big Data as mentioned in the document?',
        'options': ['A) Volume', 'B) Validity', 'C) Velocity', 'D) Variety'],
        'correct_answer': 'B) Validity',
        'detailed_explanation': {
            'A) Volume': 'Volume refers to the massive amounts of data generated daily.',
            'B) Validity': 'Correct! Validity is important but is not one of the commonly recognized Vs of Big Data.',
            'C) Velocity': 'Velocity describes the speed at which data is generated and processed.',
            'D) Variety': 'Variety indicates the diverse data formats, including structured and unstructured data.'
        }
    },
    {
        'text': 'Unstructured data in healthcare typically includes:',
        'options': ['A) Electronic medical records', 'B) Readings from medical devices', 'C) Diagnostic imaging and handwritten notes', 'D) Patient demographics stored in databases'],
        'correct_answer': 'C) Diagnostic imaging and handwritten notes',
        'detailed_explanation': {
            'A) Electronic medical records': 'EMRs are structured data, stored in databases and standardized formats.',
            'B) Readings from medical devices': 'Medical device readings are typically structured time-series data.',
            'C) Diagnostic imaging and handwritten notes': 'Correct! These types of data do not follow predefined formats, making them unstructured.',
            'D) Patient demographics stored in databases': 'Demographics are structured data, easily categorized and analyzed.'
        }
    },
    {
        'text': 'Which category of data analytics focuses on predicting future outcomes using patterns from historical data?',
        'options': ['A) Descriptive Analytics', 'B) Diagnostic Analytics', 'C) Predictive Analytics', 'D) Prescriptive Analytics'],
        'correct_answer': 'C) Predictive Analytics',
        'detailed_explanation': {
            'A) Descriptive Analytics': 'Descriptive analytics focuses on summarizing past data without predictions.',
            'B) Diagnostic Analytics': 'Diagnostic analytics determines the causes of past events rather than predicting future ones.',
            'C) Predictive Analytics': 'Correct! Predictive analytics identifies patterns to forecast future outcomes.',
            'D) Prescriptive Analytics': 'Prescriptive analytics provides recommendations but does not specifically predict future trends.'
        }
    },
    {
        'text': 'Artificial Intelligence (AI) in public health is used to:',
        'options': ['A) Store and transfer large data volumes', 'B) Mimic human intelligence to support health services', 'C) Replace healthcare workers in hospitals', 'D) Remove inconsistencies in structured data'],
        'correct_answer': 'B) Mimic human intelligence to support health services',
        'detailed_explanation': {
            'A) Store and transfer large data volumes': 'AI is not primarily used for data storage or transfer.',
            'B) Mimic human intelligence to support health services': 'Correct! AI helps in diagnosis, predictive analytics, and decision-making.',
            'C) Replace healthcare workers in hospitals': 'AI assists professionals but does not replace them.',
            'D) Remove inconsistencies in structured data': 'AI can clean data, but its role is much broader than just data consistency.'
        }
    },
    {
        'text': 'Which of the following challenges is associated with Big Data privacy risks in healthcare?',
        'options': ['A) Lack of sufficient data for analysis', 'B) Inability to access medical devices', 'C) Potential re-identification of anonymous data', 'D) Reduced accuracy of health information'],
        'correct_answer': 'C) Potential re-identification of anonymous data',
        'detailed_explanation': {
            'A) Lack of sufficient data for analysis': 'Big Data is characterized by large datasets, making data insufficiency uncommon.',
            'B) Inability to access medical devices': 'Access to medical devices is a technical issue, not a privacy risk.',
            'C) Potential re-identification of anonymous data': 'Correct! Re-identification is a major concern in healthcare privacy.',
            'D) Reduced accuracy of health information': 'Data accuracy is important but not the primary privacy concern.'
        }
    }
]

if 'current_index' not in st.session_state:
    st.session_state['current_index'] = 0

if 'answers' not in st.session_state or len(st.session_state['answers']) != len(questions):
    st.session_state['answers'] = [None] * len(questions)

if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

question = questions[st.session_state['current_index']]
st.write(question['text'])
options = question['options']
selected_option = st.radio('Choose your answer:', options, index=options.index(st.session_state['answers'][st.session_state['current_index']]) if st.session_state['answers'][st.session_state['current_index']] in options else 0)

if st.button('Submit Answer'):
    st.session_state['answers'][st.session_state['current_index']] = selected_option
    if st.session_state['current_index'] < len(questions) - 1:
        st.session_state['current_index'] += 1
    st.rerun()

if st.session_state['submitted']:
    st.write('Quiz Completed!')
    for i, question in enumerate(questions):
        st.write(f"**Question {i+1}:** {question['text']}")
        st.write(f"Your Answer: {st.session_state['answers'][i]}")
        st.write(f"Correct Answer: {question['correct_answer']}")
        for option, explanation in question['detailed_explanation'].items():
            if option == question['correct_answer']:
                st.write(f"✅ **{option}** - {explanation}")
            else:
                st.write(f"❌ **{option}** - {explanation}")
        st.write('---')
