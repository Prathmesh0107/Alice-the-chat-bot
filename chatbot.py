from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
# loading environment variables from .env file
load_dotenv()


st.set_page_config(
    page_title="Alice The AI Assistent",
      page_icon="🤖",
      layout="centered",
  
)
st.title("🤖Alice The AI Assistent chat bot")


chat_history=[]
if "chat_history"not in st.session_state:
    st.session_state.chat_history=[]

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
             st.markdown(message["content"])


llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0
    )

user_prompt=st.chat_input("im your ai helper, how can i help you?")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({ "role": "user", "content": user_prompt })

    response=llm.invoke(user_prompt)

    input=({"role":"assistent","content":"you are a helpful assistant"}),*st.session_state.chat_history

    assistent_response=response.content
    st.session_state.chat_history.append({ "role": "assistent", "content": assistent_response })    
    
    with st.chat_message("assistent"):
         st.markdown(assistent_response)



