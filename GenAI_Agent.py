import streamlit as st
from functions import *

st.set_page_config(page_title="GenAI Agent",page_icon="🤖", layout="wide") 
margin_r,body,margin_l = st.columns([0.1, 3, 0.1])

with body:
    menu()
    st.header("🤖 GenAI Agent",divider='rainbow')

    #with col1:
        #st.subheader("About Myself")
        #st.image("assets/image1.jpg", width=400)
        #st.write('Hi! This is me, Ren Hwai, chilling in Iceland. Happy family trip during my career break!')
        #st.write("My [Linkedin](https://www.linkedin.com/in/renhwai-kong/) Profile")
        #st.write("Visit my [Github](https://github.com/Ren1990?tab=repositories) projects")
        #st.write("Take a look on [Tableau](https://public.tableau.com/app/profile/kyloren.kong/viz/Demo_2024InvestmentPortfolio/DBPortfolio) viz")        
        #st.write('After working in top US semicond company for 8 years as Sr. Business Analyst and Process Development Engineer, I took a break to sharpen my Python skill in data science & analysis, and study for CFA (Chartered Finance Analyst) to look for new industry exposure and work opportunity.')
                 
    job_summary=''
    job_description=st.text_area(
        label="🤖: 'I am a Digital Twin of Ren Hwai, and I am ready for job interview.'",
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
        with st.chat_message("user",avatar="👨‍💼"):
            st.markdown(message["content"])
    if message["role"]=="assistant":
        with st.chat_message("assistant",avatar="🤖"):
            st.markdown(message["content"])

if prompt := st.chat_input("Ask me some interview questions..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user","content": prompt})
    # Display user message in chat message container
    with st.chat_message("user",avatar="👨‍💼"):
        st.markdown(prompt)

    passage=retrieve_knowledge(prompt)

    with st.chat_message("assistant",avatar="🤖"):
        response=st.write_stream(gemini_chat(make_prompt(prompt, job_summary, passage)))
        st.session_state.messages.append(
            {"role": "assistant", "content": response})
       