import streamlit as st

# Quiz questions data
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 1
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": 3
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Charles Dickens", "William Shakespeare", "J.K. Rowling", "Leo Tolstoy"],
        "answer": 1
    },
    {
        "question": "Which element is represented by the symbol 'O' in the periodic table?",
        "options": ["Oxygen", "Osmium", "Oganesson", "Obelium"],
        "answer": 0
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["1", "2", "3", "5"],
        "answer": 1
    },
    {
        "question": "Who was the first President of the United States?",
        "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"],
        "answer": 1
    },
    {
        "question": "Which gas do plants primarily absorb during photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": 2
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Gold", "Diamond", "Iron", "Platinum"],
        "answer": 1
    },
    {
        "question": "What is the longest river in the world?",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "answer": 1
    }
]

# Streamlit app layout
st.title("Quiz Application")
st.write("Test your knowledge!")

# Store the current question index and score in Streamlit's session state
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0

# Get the current question
current_question = quiz_data[st.session_state.question_index]

# Display the question and options
st.write(f"Q{st.session_state.question_index + 1}: {current_question['question']}")
options = current_question['options']
selected_option = st.radio("Choose your answer:", options)

# Handle answer submission
if st.button("Submit"):
    # Check if the selected answer is correct
    if options.index(selected_option) == current_question['answer']:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error("Incorrect.")

    # Move to the next question
    st.session_state.question_index += 1

    # Check if the quiz is finished
    if st.session_state.question_index >= len(quiz_data):
        st.write(f"Quiz finished! Your final score is {st.session_state.score}/{len(quiz_data)}")
        st.session_state.question_index = 0
        st.session_state.score = 0
    else:
        st.experimental_rerun()