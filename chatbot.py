import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain.embeddings.openai import OpenAIEmbeddings    
from langchain_openai import OpenAIEmbeddings
# from langchain.vectorstores import FAISS    
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain

# from langchain_community.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI

OPENAI_API_KEY="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"

st.header("My First Chatbot")                # UI Heading

with st.sidebar:                             # UI sidebar view
    st.title("PDF Document Input")               
    file = st.file_uploader("Upload your PDF files and ask questions from the content", type="PDF")  # Upload PDF Files

    if file is not None:
        pdf_reader = PdfReader(file)         # Extracting the text
        text=""
        for page in pdf_reader.pages:
            text+=page.extract_text()
            # st.write(text)                 # To check whether it is able to read the PDF document

                                                                    
        text_splitter = RecursiveCharacterTextSplitter(                 
            separators = "\n",
            chunk_size = 1000,
            chunk_overlap =150,
            length_function = len
        )                                    # Breaking code into Chunks

        chunks = text_splitter.split_text(text)
        # st.write(chunks)                   # To check whether the document is divided into chunks

        
        embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)  # Generating Embeddings

        vector_store = FAISS.from_texts(chunks, embeddings)    # Generating embeddings, Initialising FAISS database, Storing chunks and Embeddings
        

        user_question = st.text_input("Type your question here")
        if user_question:
            match = vector_store.similarity_search(user_question)
            st.write(match)                                    # see the question input box for asking questions
        
            llm = ChatOpenAI(
                open_api_key = OPENAI_API_KEY,
                temperature= 0,
                max_tokens= 300,
                model_name = "gpt-3.5-turbo"
            )
            chain = load_qa_chain(llm, chain_type="stuff")   # stuff everything into bucket and pass it.
            response = chain.run(input_documents =match, question = user_question, )
            st.write(response)

        