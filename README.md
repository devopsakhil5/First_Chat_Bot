# First_Chat_Bot

A minimal yet powerful chatbot that answers questions based on the content of uploaded PDF documents. Built using Streamlit, LangChain, OpenAI, and FAISS, this project demonstrates how to create an intelligent document-based Q&A system with just a few lines of code.

📌 Features
- Upload any PDF document
- Automatically splits text into manageable chunks
- Converts chunks into embeddings using OpenAI
- Stores embeddings in a FAISS vector store
- Accepts user questions via UI and retrieves relevant answers


## Block Diagram:
graph TD
    A[📄 PDF Document Upload] --> B[🔪 Text Splitting into Chunks]
    B --> C[🧠 OpenAI Embeddings]
    C --> D[📦 FAISS Vector Store]
    E[💬 User Question via UI] --> F[🔍 Query Embedding + Similarity Search]
    F --> D
    D --> G[📤 Relevant Chunks Returned]
    G --> H[🧾 Answer Generated and Displayed]


    
    
### How It Works:
- PDF Upload: User uploads a document via the Streamlit sidebar.
- Text Extraction: Text is extracted from all pages.
- Chunking: Text is split into chunks using RecursiveCharacterTextSplitter.
- Embedding: Chunks are converted into vector embeddings using OpenAI.
- Storage: Embeddings are stored in a FAISS vector store.
- Query Handling: User inputs a question; it’s embedded and compared against stored vectors.
- Answer Generation: Matching chunks are passed to the LLM to generate a response.

### Starting the Application:
As I am running the code from Github Codespace the command to run the `Streamlit` Application is: `streamlit run /workspaces/First_Chat_Bot/chatbot.py`

For running the `Streamlit` Application in localhost: `streamlit run <location_of_file_in_system>`

export OPENAI_API_KEY="your-key-here"

### Getting Started:
#### Run in GitHub Codespaces
`streamlit run /workspaces/First_Chat_Bot/chatbot.py`


#### Run Locally
`streamlit run <path_to_your_file>/chatbot.py`
 - Make sure to set your OpenAI API key as an environment variable
 - export OPENAI_API_KEY="your-key-here"



### Tech Stack:
- Streamlit
- LangChain
- OpenAI
- FAISS
- PyPDF2



