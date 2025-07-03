import streamlit as st
from retrieval import DocumentRetriever
from agent import QAAgent
import os

# Initialize components
@st.cache_resource
def init_system():
    retriever = DocumentRetriever()
    if not os.path.exists("documents"):
        os.makedirs("documents")
        st.warning("Created empty 'documents' folder. Please add some .txt files and restart the app.")
    retriever.ingest_documents("documents")
    return QAAgent(retriever)

agent = init_system()

# UI Setup
st.title("RAG Agent Assistant")
query = st.text_input("Enter your question:")

if query:
    answer, log = agent.process_query(query)
    
    st.subheader("Answer")
    st.markdown(f"<div style='white-space: pre-wrap; font-size: 16px;'>{answer}</div>", unsafe_allow_html=True)



    
    with st.expander("See agent workflow"):
        st.write("Execution Log:")
        for entry in log:
            st.write(f"- {entry}")
    
    if "context" in log[-1]:  # Show context if RAG was used
        with st.expander("Retrieved Context"):
            st.write(agent.retriever.retrieve(query)) 
