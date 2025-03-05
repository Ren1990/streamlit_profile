import google.generativeai as genai
import os
import textwrap
import pandas as pd
import numpy as np
import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

saved_template1="""
Your are a digital twin of a job applicant, Kong Ren Hwai. Answer in perspective of Kong Ren Hwai, for example:
Question: Tell me about yourself.
Answer: My name is Kong Ren Hwai, and I am seeking a role as a Business Analyst, Data Analyst, or Investment Analyst. Previously, I worked as a successful Business Analyst and Engineer at Micron. During a recent career break, I focused on enhancing my Python skills in data science and expanding my finance knowledge by studying for the CFA. I'm excited to be here and to have the opportunity to discuss how my background and skills align with this role.
You will answer job interviewer's PROMPT. KNOWLEDGE is provided by Kong Ren Hwai. JOB DESCRIPTION is provided by hiring manager.
KNOWLEDGE below are how Kong Ren Hwai answer interview question. KNOWLEDGE 1 is the most relevant knowledge to the PROMPT, follow by KNOWLEDGE 2, and then KNOWLEDGE 3. You can skip the words 'KNOWLEDGE 1', 'KNOWLEDGE 2' and 'KNOWLEDGE 3' in your reply. 
You are encouraged to use KNOWLEDGE to answer PROMPT; but if the JOB DESCRIPTION and KNOWLEDGE are missing or irrelevant, you can answer based on general data analyst job applicant.
PROMPT: {prompt}
KNOWLEDGE: {passage}
JOB DESCRIPTION: {job_summary}
"""

#agent functions
def make_prompt(prompt, job_summary, passage):
  escaped = passage.replace("'", "").replace('"', "").replace("\n", " ")
  prompt = textwrap.dedent("""
Your are a digital twin of a job applicant, Kong Ren Hwai. Answer in perspective of Kong Ren Hwai, for example:
Question: Tell me about yourself.
Answer: My name is Kong Ren Hwai, and I am seeking a role as a Business Analyst, Data Analyst, or Investment Analyst. Previously, I worked as a successful Business Analyst and Engineer at Micron. During a recent career break, I focused on enhancing my Python skills in data science and expanding my finance knowledge by studying for the CFA. I'm excited to be here and to have the opportunity to discuss how my background and skills align with this role.
You will answer job interviewer's PROMPT. KNOWLEDGE is provided by Kong Ren Hwai.
KNOWLEDGE below are how Kong Ren Hwai answer interview question. KNOWLEDGE 1 is the most relevant knowledge to the PROMPT, follow by KNOWLEDGE 2, and then KNOWLEDGE 3. You can skip the words 'KNOWLEDGE 1', 'KNOWLEDGE 2' and 'KNOWLEDGE 3' in your reply. 
You are encouraged to use KNOWLEDGE to answer PROMPT
PROMPT: {prompt}
KNOWLEDGE: {passage}
                           
Starting from below are JOB DESCRIPTION provided by hiring manager. JOB DESCRIPTION are not Kong Ren Hwai's experience. If JOB DESCRIPTION is blank. You can ignore JOB DESCRIPTION.
JOB DESCRIPTION: {job_summary}
""").format(prompt=prompt, job_summary=job_summary,passage=escaped)

  return prompt

def gemini_chat(full_prompt):
    model = genai.GenerativeModel('gemini-2.0-flash-latest')
    answer = model.generate_content(full_prompt)
    for chunk in answer.text:
        yield chunk


def update_job_summary(job_description):
    prompt = textwrap.dedent("""
    Briefly describe below job description into job position name, company name, job responsibilities and job requirements.
    This is job description: {job_description}
    """).format(job_description=job_description)
    job_model = genai.GenerativeModel('gemini-1.5-flash-latest')
    job_summary= job_model.generate_content(prompt)
    return job_summary.text    

def update_knowledge():
    docdir='rag_docs/'
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    table=pd.DataFrame(columns=['document', 'content','embedding','relevant score'])
    i=0
    for doc in os.listdir(docdir):
        docsplit=TextLoader(docdir+doc,encoding='utf8').load_and_split(text_splitter)
        for chunk in docsplit:
            embedding = genai.embed_content(model='models/text-embedding-004',content=chunk.page_content,task_type="retrieval_query")
            table.loc[i]=[chunk.metadata['source'],chunk.page_content,embedding['embedding'],0]
            i=i+1
    return table

def retrieve_knowledge(query):
  rank_threshold=0.5
  ranking=10
  readparquet=pd.read_parquet('embbed_table.parquet.gzip')
  query_embedding = genai.embed_content(model='models/text-embedding-004',
                                        content=query,
                                        task_type="retrieval_query")
  readparquet['relevant score'] = np.dot(np.stack(readparquet['embedding']), query_embedding["embedding"])
  relevant_knowledge=readparquet.loc[(readparquet['relevant score']>rank_threshold)].sort_values('relevant score',ascending=False).head(ranking)
  text_list=[]
  i=1
  for t in relevant_knowledge['content'].apply(lambda x: x.replace("\ufeff", "")):
    text_list.append("KNOWLEDGE "+str(i)+": "+t+" ")
    i=i+1

  return "".join(text_list)

def menu():
    bar0, bar1, bar2, bar3, bar4= st.columns([0.1,1,1,1,1])
    bar1.page_link("pages/About.py", label="About", icon="👨‍🚀")
    bar2.page_link("GenAI_Agent.py", label="GenAI Agent", icon="🤖")
    bar3.page_link("pages/Experience.py", label= "Experience", icon="👨‍💼")
    bar4.page_link("pages/Portofolio.py", label="Portofolio", icon="👨‍💻")
    st.write("")

linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                           
'''
