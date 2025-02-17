from typing import Annotated, Literal
from autogen import ConversableAgent

config_list = [
        {
            # Let's choose the model
            "model": "qwen2.5:latest",
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama",
        }
]

Operator = Literal["+", "-", "*", "/"]

def calculator(a: int, b:int, operator: Annotated[Operator, "Operator"]) -> int:
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return int(a / b)
    else:
        raise ValueError("Invalid operator")

assistant = ConversableAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant. "
    "You can help with simple calculations. "
    "Return 'TERMINATE' when the task is done.",
    llm_config={"config_list": config_list},
)

user_proxy = ConversableAgent(
    name="User",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)

assistant.register_function(
    function_map={
        "calculator": calculator
    }
)

chat_result = user_proxy.initiate_chat(assistant, message="What is (44232 + 13312 / (232 - 32)) * 5?")