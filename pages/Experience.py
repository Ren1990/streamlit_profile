import streamlit as st
from functions import *

st.set_page_config(page_title="Experience", page_icon="👨‍💼", layout="wide")
margin_r,body,margin_l = st.columns([0.1, 3, 0.1])

with body:
    menu()
    st.header("👨‍💼 Experience",divider='rainbow')
    st.write("")
    col1,  col2 = st.columns([3,2])
    with col1:
        st.subheader(":blue[Sr. Business Analyst | Micron Semiconductor Asia]", divider='grey')
    with col2:
        st.subheader("2022 Mar - 2024 Jan", divider='grey')
    st.markdown("##### **AI Transformation | Stakeholder Management | Visualization | GenAI | Snowflake | Bigquery | Agile**")
    st.markdown("Reported directly to the Director and regularly provided executive summaries and presentations to VPs from various organizations. Collaborated with cross-functional teams to identify and analyze bottlenecks and gaps in resource planning, technical development, and infrastructure architecture. Below are key projects I managed:")
    st.markdown("#### **Virtual Metrology Prediction with Machine Learning:**")
    st.markdown("""
                - Led a data science team in leveraging equipment signals (e.g., pressure, voltage, process time) to train machine learning models for predicting critical wafer output metrics such as deposition thickness and etching depth.
                - **Objective:** Achieved 100% product quality coverage without additional CAPEX for metrology tools while reducing cycle time.
                - **Achievements:** Demonstrated models with RMSE (root mean squared error) <10% of process standard deviation, validated by production data. Integrated Virtual Metrology into the SPC system for enhanced statistical process control and quality assurance.
                - **Business Impact:** Supported the ramp-up of specialized AI memory chip production, outpacing competitors to secure several hundred million dollars in revenue by 2024 and maintaining a full order book through 2025.
                """)
    st.link_button("Read the news", "https://www.yahoo.com/tech/micron-says-high-bandwidth-memory-180015907.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAJDlZc7jpuruOELXv_OcCaEPJ4f_DWLuKu6mqUCmetwC9l6PdEdgI5mXZ0BEDlS6jTFpd6dpdG8OkiUjJz34sqB7mSGVbK457AkSurmtO7d5I_RUN4znrdV9590DA4jYniYiwXJMVBvI55GX2ikf-sjVT6S7d6pF-juDBZyiJ84c]")
    st.markdown("#### **Smart Search Assistant Powered by GenAI:**")
    st.markdown("""
                - Developed and implemented an Enterprise Smart Search Assistant powered by GenAI in collaboration with global departments, integrating it across multiple data systems.
                - **Objective:**  Enhanced workforce productivity by optimizing internal data search capabilities with enhanced security to prevent sensitive data leak.
                - **Achievements:** Established robust ETL (Extract, Transform, Load) pipelines and RAG (Retrieval Augmented Generation) frameworks for efficient data retrieval and summarization.  Significantly improved decision-making processes across departments by eliminating traditional information-gathering delays.
                """)
    st.link_button("Read the blog", "https://sg.micron.com/about/blog/applications/ai/generative-ai-wave-of-innovation]")
    st.write("")
    col1,  col2 = st.columns([3,2])
    with col1:
        st.subheader(":blue[Sr. Process Engineer | Micron Semiconductor Asia]", divider='grey')
    with col2:
        st.subheader("2015 July - 2022 March", divider='grey')
    st.markdown("##### **Root Cause Analysis | Problem Solving | Risk Management | Design of Experiment | Data Mining**")
    st.markdown("Highlighted data analytic skills:")
    st.markdown("#### **Problem Solving with Data:**")
    st.markdown("""
                - Applied statistical Design of Experiment (DOE) methodology to conduct comprehensive evaluations, identifying and resolving critical failures encountered during on-device HAST reliability tests for key mobile phone customers.
                - Mitigated potential losses amounting to hundreds of millions by ensuring successful new product launches.
                """)
    st.markdown("#### **Data Mining:**")
    st.markdown("""
                - Utilized robust data mining and failure analysis techniques to pinpoint wafer deviations originating from frontend wafer fabrication processes. 
                - Spearheaded a continuous improvement initiative that delivered a significant ~4% weekly yield gain, enhancing production efficiency and product quality.
                """)
