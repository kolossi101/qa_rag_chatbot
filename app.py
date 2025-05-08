import os
import streamlit as st
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from src.prompt import *


load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
HF_API_KEY = os.environ.get("HF_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["HF_API_KEY"] = HF_API_KEY

embeddings = download_hugging_face_embeddings()

#Change the following index name if needed
index_name = "infobot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings,
)

client = InferenceClient(
    provider="nebius",
    api_key=HF_API_KEY,  
)

def chat_with_qwen(question, context):
    messages = [
        {"role": "system", "content": prompt_template},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
    ]
    
    completion = client.chat.completions.create(
        model="microsoft/phi-4", 
        messages=messages, 
        max_tokens=500,
    )
    
    return completion.choices[0].message["content"]  


def retrieval_qa_chain(question):
    # Retrieve relevant documents
    retrieved_docs = docsearch.similarity_search(question, k=10)
    context = " ".join([doc.page_content for doc in retrieved_docs])
    print(f"\n\n***The following is the context supplied to the model***:\n\n{context}")
    # Generate answer using the model
    answer = chat_with_qwen(question, context)

    return {"question": question, "answer": answer, "source_documents": retrieved_docs}


st.title("Biochemistry Q&A")
with st.form("my_form", clear_on_submit=True):
    user_input = st.text_input("Ask me something:")
    submitted = st.form_submit_button("Send") 
    if submitted:
        if user_input:
            with st.spinner("Generating response..."):
                response = retrieval_qa_chain(user_input)
                st.markdown(f"**You:** {user_input}")
                st.markdown(f"**Bot:** {response['answer']}")

