import google.generativeai as genai
import os
import textwrap
import pandas as pd
import numpy as np
import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

skill_col_size = 5

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
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    answer = model.generate_content(full_prompt)
    for chunk in answer.text:
        yield chunk


def update_job_summary(job_description):
    prompt = textwrap.dedent("""
    Briefly describe below job description into job position name, company name, job responsibilities and job requirements.
    This is job description: {job_description}
    """).format(job_description=job_description)
    job_model = genai.GenerativeModel('gemini-1.0-pro')
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

#design layout
def menu():
    bar0, bar1, bar2, bar3, bar4= st.columns([0.1,1,1,1,1])
    bar1.page_link("pages/3_🌏_Contacts.py", label="Contacts", icon="🌏")
    bar2.page_link("GenAI_Agent.py", label="GenAI Agent", icon="🤖")
    bar3.page_link("pages/Working_Experience.py", label= "Working Experience", icon="💼")
    bar4.page_link("pages/Portofolio.py", label="Portofolio", icon="👨‍💻")
    st.write("")

#publication_url --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
linkedin_logo = '''                                                                                                                                          
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-linkedin" style="font-size: 28px;"></i>                                                                           
'''

github_logo = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <i class="fa-brands fa-github" style="font-size: 28px;"></i>                                                                           
'''

# personal info (for main page) --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
info = {'brief':
              """    
                Starting from physical therapist, to UX designer, to software engineer and product manager... 
                I am a passionate and curious explorer currently pursuing a Computer Science and Anthropology major at Brandeis University, expected to graduate in May 2025.
                **I believe in the intersectionality of quantitative and qualitative subjects, that neither approach alone can lead one to the absolute truth.**
              """,
        'name':'Haoran cheng', 
        'study':'Brandeis University',
        'location':'Boston, MA',
        'interest':'Full Stack, Data Science, Product Management',
        'skills':['Python','Java','Javascript','Typescript','Shell','HTML & CSS','React','Node.js','Tableau','Streamlit','PySpark','Svelte','Docker','Kafka','Kubernetes','MongoDB','PostgreSQL','MySQL','SQLite','AWS','Github','Gitlab','Figma','OpenAI API','Excalidraw','Trello','REST api','HTTP'],
        }


# Portfolio --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#     {'project1':[HEADER, CONTENT]
#      'project2':[HEADER, CONTENT]
#      ...}

Portfolio = { 1:[':blue[Deis]Evaluation - Course Evaluation Website',
              """
              Launched a course evaluation web app for Brandeis students to review and share courses, exceeding 200+ active users.
              Designed the whole UI with Figma and Implemented front end with Javascript, HTML/CSS in a MERN Stack.
              """],
              2:['Data Visualization in :orange[D3.js]',
                  """
                Created a data visualization web app for Massachusetts police expenditure data using D3.js.
                """],
              3:[':blue[LLM] Desktop ChatApp',
                """
                - Designed and developed a cross-platform **desktop LLM Chat app**, enabling chat over user-upload dataset; providing a more accurate response to domain-specific inquiries than ChatGPT.
                - Utilized Embedding and Searching from **OpenAI API** to optimize Chat app’s response. Split the user-upload file into small chunks; used OpenAI Embedding model to vectorize each chunk and save them into Qdrant database. Transform user query to vector using OpenAI, and then inquire the top match text chunk from Qdrant database using topk value.
                """],
              4:[':orange[Anthropology] Research Project - A Timeless Building',
                """
                - An **qualitative anthropological research** on the preservation and adaption of historical sites; as final project, received the highest score in class.
                - My fieldwork includes interviewing educators, examing archive, on-site obervation. Through my fieldwork at King’s Chapel, I argued for a humane approach to preserving historic sites, that seeks a balance between **maintaining the historical significance and the sites’ adaptations to societal changes**.
                """],
              5:[':green[RAG] playground',  
                """
                - Developed a **RAG** chatbot that support difference choices over Embedding model, chunking strategy, top k retreival, LLM model, prompt engineering, and meta-data retreival search.
                - Implemented the file uploading workflow; Utilized **Langchain splitter** module and Python script to clean and chunk the uploaded file and use Huggingface sentence transformers and **Pinecone** to vectorize and store data.
                - Used SpaCy NER model to retreive meta data from prompt and ran a hybrid search using meta-data and vector.
                """]
            }
              
# Contacts --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
phone = "971-900-6780"
email = "haorancheng@brandeis.edu"
linkedin_link = "www.linkedin.com/in/haoran-cheng/"
github_link = "https://github.com/Rsirp0c?tab=repositories"


# iframes --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
figma_iframe = '<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1" allowfullscreen></iframe>'

figma_link = "https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FlMYyNOptCmZb5JlYXmKkif%2FCourseEvaluation%3Ftype%3Ddesign%26node-id%3D160%253A1249%26mode%3Ddesign%26t%3DEj6BVdYEZCLgxthB-1"

StoryMap_iframe = "https://storymaps.arcgis.com/stories/dfb9689618e343cf9f6ef36d9a8329a7?header"

Evaluation_html = '''
                <div class="github-card" data-github="Rsirp0c/deis-course-evaluation" data-width="400" data-height="" data-theme="default"></div>
                <script src="https://cdn.jsdelivr.net/github-cards/latest/widget.js"></script>                
                '''
