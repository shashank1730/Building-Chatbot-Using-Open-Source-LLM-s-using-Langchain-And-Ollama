import streamlit as st
import os
from langchain_groq import ChatGroq

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time


from dotenv import load_dotenv
load_dotenv(dotenv_path="../.env")

groq_api_key = os.environ['GROQ_API_KEY']

if "vector" not in st.session_state:
    # Here we are using Ollama Embeddings for filling the text
    st.session_state.embeddings = OllamaEmbeddings()
    # Extracting the wen URL content
    st.session_state.loader = WebBaseLoader("https://www.aa.com/i18n/customer-service/support/legal-information.jsp")
    # Loading the URL content
    st.session_state.docs = st.session_state.loader.load()
    # setting up the chuck size for Splitting the content into chucks 
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap = 200)
    # finally spliting the content into chunks
    st.session_state.final = st.session_state.text_splitter.split_documents(st.session_state.docs)
    # Storing the data in FAISS vector DB 
    st.session_state.faiss_vector = FAISS.from_documents(st.session_state.final, st.session_state.embeddings)

st.title("American Airlines Refund Agent")
# Using "Gemma" Google gemini's best model
llm = ChatGroq(groq_api_key=groq_api_key,
               model_name = "mistral-saba-24b")

prompt = ChatPromptTemplate.from_template(
    """
    But if the question is releated to american airlines baggage/refund/terms & conditions then You are a helpful customer service assistant trained on American Airlines policies.

Step 1: but if you are answering from the <context> tell the cusomter confidentely I have checked the Terms and conditons for you and this is what I found
Step 2: Try to find the answer in the provided context. Quote relevant policy lines when possible never tell customer to go check this part for more info.
Step 3: If the answer is NOT found in the context, use your general airline knowledge, but mention that you're doing so 


<context>
{context}
</context>

Question: {input}
    """
)

document_chain = create_stuff_documents_chain(llm,prompt)
retriever = st.session_state.faiss_vector.as_retriever()
retriever_chain = create_retrieval_chain(retriever,document_chain)

prompt = st.text_input("Enter any trouble/query realted to American Airlines")



if prompt:
    start = time.process_time()
    response = retriever_chain.invoke({"input": prompt})
    print("Response Time :", time.process_time()-start)
    st.write(response['answer'])



