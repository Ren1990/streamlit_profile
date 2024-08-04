import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from streamlit_extras.stylable_container import stylable_container
import streamlit.components.v1 as components
from functions import *
st.set_page_config(page_title="Portofolio", page_icon="👨‍💻", layout="wide")
margin_r,body,margin_l = st.columns([0.1, 3, 0.1])

with body:
   menu()
   st.header("👨‍💻 Portfolio")
   st.write("")
   st.subheader(":blue[1. Bank Customer Subscription Prediction - Binary Classification Model Demo:]", divider='grey')
   col1,  col2 = st.columns([3,2.4])
   with col1:
      st.markdown("##### Machine Learning | Data Cleaning| Analysis | Visualization | Python | Scikit | XGBoost | Cross Validation | Optuna | Matplot | Plotly")
      st.markdown("""
                  - **Objective:** Developed a binary classification model using an open Kaggle dataset to predict whether a bank customer would subscribe to a term deposit during a marketing campaign.
                  - **Challenge:** Addressed data imbalance with only 11% successful subscriptions by choosing balanced accuracy as the performance metric.
                  - **Achievement:** Achieved a balanced accuracy of 83% with a recall of 70%. Identified the most critical factor influencing the outcome: the duration since the last marketing campaign with the customer.
                  - **Presentation Slide:** [Bank Term Deposition Subscription Prediction](https://docs.google.com/presentation/d/1hGG3yMfugKGOfFKQ-XcSUYOL7bIE1J2XIRnxq0ROVEQ/edit#slide=id.g274072545a7_0_1) 
                  - [Github](https://github.com/Ren1990/bank_term_deposit_clf_model) 
                  """)
   with col2:
      with stylable_container(
         key='port1',
         css_styles=[
            """
         {
            border: 2px solid #CCCCCC;
         }
         """
         ]
      ):
         pdf_viewer("assets/Bank Term Deposition Subscription Prediction.pdf",width=720,height=400)

   st.write("")
   st.subheader(":blue[2. House Prices Prediction - Regression Model Demo:]", divider='grey')
   col1,  col2 = st.columns([3,2.4])
   with col1:
      st.markdown("##### Machine Learning | Data Cleaning| Analysis | Visualization | Python | Scikit | XGBoost | GradientBoost | Time-Based Cross Validation | Optuna | Matplot | Plotly ")
      st.markdown("""
                  - **Objective:** Built a regression model using an open Kaggle dataset to predict house prices in the US. RMSE is chosen as the model performance metric to prioritize in reducing prediction error.
                  - **Challenge:** Set RMSE target to be less than 30% of the standard deviation (\$23,833) based on the mean sale price (\$180,921) and standard deviation (\$79,442).
                  - **Achievement:** Initial Gradient Boosting model achieved an RMSE of \$25,367 (31.9% of standard deviation). Enhanced the model to a Time-Based Split XGBoost Regression, achieving an RMSE of \$22,619, meeting the target criteria.
                  - **Presentation Slide:** [House Price Prediction Modeling](https://docs.google.com/presentation/d/1d3QmS1A7Vqn16JUQmDEF7P3PND2N7QLmmtiNEIG28h8/edit#slide=id.g274a5d39379_0_59) 
                  - [Github](https://github.com/Ren1990/house_price_reg_model) 
                  """)
   with col2:
      with stylable_container(
         key='port1',
         css_styles=[
            """
         {
            border: 2px solid #CCCCCC;
         }
         """
         ]
      ):
         pdf_viewer("assets/House Price Prediction Modeling.pdf",width=720,height=400)

   st.write("")
   st.subheader(":blue[3. GenAI: Digital Twin Job Interviewee Agent Hosted by Streamlit:]", divider='grey')
   col1,  col2 = st.columns([3,2.4])
   with col1:
      st.markdown("##### LLM | RAG | Prompt Engineering | Streamlit | Python")
      st.markdown("""
                  - **Objective:** Demonstrate the use case of Generative AI by creating a personal Digital Twin Job Interviewee Agent to interact with recruiters and hiring managers. Utilizing prompt engineering, the Agent will retrieve my personal knowledge data (e.g., my resume, sample interview answers) through the Retrieval Augmented Generation (RAG) framework and use the relevant information to respond effectively.
                  - **Challenge:** While prompt engineering is valuable for shaping LLM responses, the format and quality of the RAG documents are equally crucial. To ensure high-quality conversational responses, I have learnt that transforming my RAG documents from bullet-point lists into a more conversational format is the most effective approach. Another challenge I encountered is the issue of chat memory. The Agent sometimes struggles to respond effectively to previous conversations. This could potentially be resolved by using a long-context Language Model (LLM) that can maintain a better memory of past interactions.
                  - **Streamlit demo web link:** [🤖 GenAI Agent](https://renhwaichatbot.streamlit.app/) 
                  - [Github](https://github.com/Ren1990/genai_job_candidate_agent) 
                  """)
   with col2:
      components.iframe("https://renhwaichatbot.streamlit.app/~/+/", width=750, height=400)
   
   st.write("")
   st.subheader(":blue[4. Tableau: 2024 Investment Portfolio:]", divider='grey')
   col1,  col2 = st.columns([3,2.3])
   with col1:
      st.markdown("##### Tableau | Data Storytelling | Interactive Visualization | Investment")
      st.markdown("""
                  - **Objective:** Create an interactive Tableau visualization to illustrate a 2024 high-growth portfolio allocation that balances growth from stocks in emerging industries and diversifies risk with long-maturity U.S. Treasuries in anticipation of a Federal Reserve rate cut.
                  """)
      st.link_button("Go to Tableau Public", "https://public.tableau.com/app/profile/kyloren.kong/viz/Demo_2024InvestmentPortfolio/DBPortfolio")



