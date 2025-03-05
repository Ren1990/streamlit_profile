import streamlit as st
from functions import *

st.set_page_config(page_title="GenAI Agent",page_icon="🤖", layout="wide") 
margin_r,body,margin_l = st.columns([0.1, 3, 0.1])

with body:
    menu()
    st.header("🤖 GenAI Agent",divider='rainbow')     
    job_summary=''
    job_description=st.text_area(
        label="🤖: 'I am a Digital Twin of Ren Hwai, and I am ready for job interview!'",
        placeholder ="You can paste a job description here, or skip to the bottom to ask question.",
        height=250,
        )
    if job_description!='':
        job_summary= update_job_summary(job_description)
   
#Main chat
    if job_summary!='':
        st.write(job_summary)
    st.subheader("Begin interview here...",divider='rainbow')

if "messages" not in st.session_state:
    #st.session_state.table=update_knowledge()
    st.session_state.messages = []
    

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"]=="user":
        with st.chat_message("user",avatar="🧒🏻"):
            st.markdown(message["content"])
    if message["role"]=="assistant":
        with st.chat_message("assistant",avatar="🤖"):
            st.markdown(message["content"])

if prompt := st.chat_input("Ask me some interview questions..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user","content": prompt})
    # Display user message in chat message container
    with st.chat_message("user",avatar="🧒🏻"):
        st.markdown(prompt)

    passage=retrieve_knowledge(prompt)

    with st.chat_message("assistant",avatar="🤖"):
        st.write(prompt)
        response=st.write_stream(gemini_chat(make_prompt(prompt, job_summary, passage)))
        st.session_state.messages.append(
            {"role": "assistant", "content":response})
       
