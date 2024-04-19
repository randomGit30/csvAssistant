import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import pandas as pd
def main():
    load_dotenv()
    st.set_page_config(page_title="AI assistant")
    st.header("CSV Assistant")
    user_csv = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if user_csv is not None:
        st.write("File uploaded successfully 👍")
        user_question = st.text_input("Ask a question: ")

        llm = ChatGoogleGenerativeAI(model="gemini-pro",verbose = True,temperature = 0,google_api_key="AIzaSyDVfBImmUr-rxM9PPKnevbkyhi2f-yD5KU")
        agent = create_csv_agent(llm, user_csv, verbose=True)

        if user_question is not None and user_question != "":
            response = agent.run(user_question)
            st.write(response)


if __name__ == "__main__":
    main()
