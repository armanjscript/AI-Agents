import os
from textwrap import dedent
from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

load_dotenv()

# Set your API keys
os.environ["GROQ_API_KEY"] = "YOUR_GROQ_API_KEY"
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"  # Add your OpenAI API key here
os.environ["GEMINI_API_KEY"] = "YOUR_GOOGLE_API_KEY"

llm = LLM(
    model="ollama/qwen2.5:latest",
    base_url="http://localhost:11434",
    temperature=0.5,
)

class GameAgents:
    def senior_engineer_agent(self):
        return Agent(
            role = "Senior Software Engineer",
            goal = "Create software as needed",
            backstory = dedent("""\
                You are a Senior Software Engineer at a leading tech tik tank.
                Your expertise in programming in python. and do your best to
                produce perfect code"""),
            allow_delegation=False,
            llm = llm,
            verbose = True
        )
    
    def qa_engineer_agent(self):
        return Agent(
            role = "Software Quality Control Engineer",
            goal = "Create Perfect code, by analyzing the code that is given for errors",
            backstory = dedent("""\
                You are a software engineer that specializes in checking code 
                for errors. You have an eye for detail and knack for finding 
                hidden bugs.
                You check for missing imports, variable declarations, mismatched 
                brackets and syntax errors. 
                You also check for security vulnerabilities, and logic errors."""),
            allow_delegation=False,
            llm = llm,
            verbose = True
        )
    
    def chief_qa_engineer_agent(self):
        return Agent(
            role = "Chief Software Quality Control Engineer",
            goal = "Ensure that the code does the job that it is supposed to do",
            backstory = dedent("""\
                You feel that programmers always do only half the job, so you are 
                super dedicate to make high quality code."""),
            allow_delegation=True,
            llm = llm,
            verbose = True
        )