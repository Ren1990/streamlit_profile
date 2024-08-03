import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import streamlit.components.v1 as components
from functions import *
st.set_page_config(page_title="Portofolio", page_icon="👨‍💻", layout="wide")
margin_r,body,margin_l = st.columns([0.1, 3, 0.1])

with body:
   menu()
   st.header("👨‍💻 Portfolio")
   st.write("")
   st.subheader(":blue[1. Bank Customer Subscription Prediction - Binary Classification Model Demo:]", divider='grey')
   col1,  col2 = st.columns([3,2])
   with col1:
      st.markdown("##### Machine Learning | Data Cleaning| Analysis | Visualization | Python | Scikit | XGBoost | Cross Validation | Optuna | Matplot | Plotly")
      st.markdown("""
                  - **Objective:** Developed a binary classification model using an open Kaggle dataset to predict whether a bank customer would subscribe to a term deposit during a marketing campaign.
                  - **Challenge:** Addressed data imbalance with only 11% successful subscriptions by choosing balanced accuracy as the performance metric.
                  - **Achievement:** Achieved a balanced accuracy of 83% with a recall of 70%. Identified the most critical factor influencing the outcome: the duration since the last marketing campaign with the customer.
                  - Presentation Slide: [Bank Term Deposition Subscription Prediction](https://docs.google.com/presentation/d/1hGG3yMfugKGOfFKQ-XcSUYOL7bIE1J2XIRnxq0ROVEQ/edit#slide=id.g274072545a7_0_1) 
                  - [Github](https://github.com/Ren1990/bank_term_deposit_clf_model) 
                  """)
   with col2:
      st.markdown("##### Project Presentation")
      pdf_viewer("assets\Bank Term Deposition Marketing Campaigns Outcome Prediction Modeling.pdf",width=700,height=350)
      

