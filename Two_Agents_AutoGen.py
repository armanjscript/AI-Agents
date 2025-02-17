from autogen import ConversableAgent
import streamlit as st

config_list = [
        {
            # Let's choose the model
            "model": "qwen2.5:latest",
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama",
        }
]

st.title("AutoGen example of conversation patter or two agents")

def student_teacher_chat():
    student_agent = ConversableAgent(
        name="Student_Agent",
        system_message="You are a student willing to learn",
        llm_config={"config_list": config_list},
        human_input_mode="ALWAYS"
    )

    teacher_agent = ConversableAgent(
        name="Teacher_Agent",
        system_message="You are a math teacher.",
        llm_config={"config_list": config_list},
    )


    chat_result = "NULL"
    if query:= st.chat_input("Enter your queries to teacher"):
        chat_result = student_agent.initiate_chat(
            teacher_agent,
            message=query,
            summary_method="reflection_with_llm",
            max_turns=2
        )
        for messages in chat_result.chat_history:
            st.write(messages)

student_teacher_chat()