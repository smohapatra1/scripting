#   Create a chatbot 

import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI

open_api_keys = "text1234"

st.header("My First chatbot")
with st.sidebar:
    st.title("Your document")
    file = st.file_uploader("Upload a PDF file and start asking question", type="pdf")

if file is None:
    prf_reader = PdfReader(file)
    text = ""
    for page in prf_reader.pages:
        text +=page.extract_text()
        # st.write(text)

text_splitter = RecursiveCharacterTextSplitter( 
    separators= "\n", 
    chunk_size = 1000, 
    chunk_overlap = 150, 
    length_function = len)
chunks = text_splitter.split_text(text)
st.write(chunks)

embedding = OpenAIEmbeddings(openai_api_key = open_api_keys)
vector_store = FAISS.from_text(chunks, embedding)

user_input = st.text_input("Type your questions")
if user_input:
    match = vector_store.similarity_search(user_input)
    st.write(match)
    llm = ChatOpenAI(
        keys = open_api_keys, 
        temp = 0, 
        max_tokens = 1000, 
        model_name = "text1"

    )
    chain = load_qa_chain(llm, chain_type = "stuff")
    response = chain.run(input_documents= match, questions = user_input)
    st.write(response)

