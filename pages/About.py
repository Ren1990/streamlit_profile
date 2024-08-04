import streamlit as st 
from functions import *

st.set_page_config(page_title="About", page_icon="👨‍🚀",layout="wide") #
margin_r,body,margin_l = st.columns([0.1, 3, 0.1])

with body:
    menu()
    st.header("👨‍🚀 About",divider='rainbow')
    st.write("")
    colA,  colB = st.columns([2.5,3])
    with colA:
        st.image("assets/image1.jpg", width=600)
        st.write('Hi! This is me, Ren Hwai, chilling in Iceland. Happy family trip during my career break!')
        st.write('After working in top US semicond company for 8 years as Sr. Business Analyst and Process Development Engineer, I took a break to sharpen my Python skill in data science & analysis, and study for CFA (Chartered Finance Analyst) to look for new industry exposure and work opportunity.')
        st.markdown(f"##### ✉️  Email: kongrenhwai@hotmail.com")
    with st.container():
        col1, col2 = st.columns([0.1, 3])
        with col1:
            st.write(linkedin_logo, unsafe_allow_html=True)
        with col2:
            st.markdown(f"##### Linkedin: {'https://www.linkedin.com/in/renhwai-kong/'}")
    with st.container():
        col1, col2 = st.columns([0.1, 3])
        with col1:
            st.write(github_logo, unsafe_allow_html=True)
        with col2:
            st.markdown(f"##### Github: {'https://github.com/Ren1990?tab=repositories'}")
    with colB:
        st.subheader(':blue[Business Analyst]')
        st.markdown('##### **Gap Analysis | Leadership Reporting | Stakeholder Influencing | Resource Planning | Data-Driven Decision Making | Agile | Scrum | JIRA | Confluence**')
        st.subheader(':blue[Data Analyst & Data Scientist]')
        st.markdown('##### **Data Analytic | Visualization | Machine Learning | Data Mining | SQL | GenAI | Python | SpotFire | Tableau | Snowflake | Google Bigquery | GCP**')
        st.subheader(':blue[Semiconductor Engineer]')
        st.markdown('##### **Problem Solving | Risk Management & Planning | New Product Introduction | Technology Development | Process Control | DOE | FMEA | JMP**')
        st.subheader(':blue[Finance Knowledge]')
        st.markdown('##### **Finance Statement | Discounted Cash Flow Valuation | Residual Income Valuation | Equity Research | Economy | Stock | Fixed Income | Future | Option**')