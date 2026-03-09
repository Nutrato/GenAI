import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Suppress the warning when running in development
import warnings
warnings.filterwarnings("ignore", message=".*missing ScriptRunContext.*")

key = "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"

st.header("PDF Text Extractor")

with st.sidebar:
    st.title("Upload your PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        # st.write(text)

    # Display the extracted text
    # st.subheader("Extracted Text:")
    # st.text_area("PDF Content", text, height=400)

    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len
        )
    chunks = text_splitter.split_text(text)
    # st.write(chunks)
    # for i, chunk in enumerate(chunks):
    #     st.write(f"Chunk {i + 1}:")
    #     st.write(chunk)

    # generating the emmbeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=key)

    # creating vector store -FAISS
    vector_store = FAISS.from_texts(chunks, embeddings)

    # get user query
    user_query = st.text_input("Ask a question about the PDF content:") 

    #do similarity search
    if user_query:
        results = vector_store.similarity_search(user_query)
        st.write(f"Search Results:{results}")