import os
os. environ["STREAMLIT_WATCHER_TYPE"] = "none"
import streamlit as st
import time
import google.generativeai as genai
from langchain_community.document_loaders import PyPDFLoader # pdf loader for loading pdf files 
from langchain. text_splitter import RecursiveCharacterTextSplitter # Text splitter for chunking documents
from langchain_chroma import Chroma # Vector Database for embeddings
from langchain_huggingface import HuggingFaceEmbeddings # Embedding model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

st.title("RAG Application built on Gemini Model for Social Studies 10th standard")

api_key= os.environ.get('GEMINI_API_KEY')
model_name = os.environ.get('MODEL_GEMINI')

genai.configure(api_key=api_key)

#load the pof file
loader = PyPDFLoader("C:\\Users\\reena\\OneDrive\\Desktop\\RAG_APP\\rag_poc\\TM_Social_EM.pdf")
data = loader.load()

# spliting the data into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=300,
    length_function=len
)

docs = text_splitter.split_documents(data)


# storing the embedding in the vector database

vectorstore = Chroma.from_documents(documents=docs, embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 10})

# chat with the model
print(' model name---', model_name)

llm = ChatGoogleGenerativeAI(model=model_name, temperature=0, google_api_key=api_key, max_tokens=None, timeout=None)

query = st.chat_input("Ask something: ")
prompt = query

system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you"
    "don't know. Use ten sentences maximum and keep the "
    "answer concise. Format your response in bullet points."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human","{input}"),
    ]
)

if query:
    with st.spinner( "Generating response..."):
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        response = rag_chain.invoke({"input": query})
    st. write("*Question:*", query)
    st. write(response["answer"])