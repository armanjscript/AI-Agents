import streamlit as st
from crewai import Crew
from tasks import GameTasks
from agents import GameAgents


#Load the tasks
tasks = GameTasks()
agents = GameAgents()

#Streamlit app
def game_builder_app():
    st.title("Game Crew")
    st.write("## Welcome to the Game Development Crew")
    
    #Input for the game and mechanics
    game = st.text_input("What is the game you would like to build? What will be the mechanics?", placeholder="Enter the game")
    
    #Button for building game
    if st.button("Build the Game"):
        if game:
            #Create agents
            senior_engineer_agent = agents.senior_engineer_agent()
            qa_engineer_agent = agents.qa_engineer_agent()
            chief_qa_engineer_agent = agents.chief_qa_engineer_agent()
            
            #Create tasks
            code_game = tasks.code_task(senior_engineer_agent, game)
            review_game = tasks.review_task(qa_engineer_agent, game)
            approve_game = tasks.evaluate_task(chief_qa_engineer_agent, game)
            
            #Create Crew
            crew = Crew(
                agents = [
                    senior_engineer_agent,
                    qa_engineer_agent,
                    chief_qa_engineer_agent
                ],
                tasks=[code_game, review_game, approve_game],
                verbose=True,
            )
            
            game_result = crew.kickoff()
            st.write("### Here is the result")
            st.write("### Final code for the game:")
            st.write(game_result)
            
        else:
            st.warning("Please provide details about the game and its mechanics.")
            
if __name__ == "__main__":
    game_builder_app()