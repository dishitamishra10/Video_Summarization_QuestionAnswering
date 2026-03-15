from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def create_vectorstore(transcript: str):
    splitter = RecursiveCharacterTextSplitter(
	    chunk_size=700,
	    chunk_overlap=170
    )

    chunks = splitter.create_documents([transcript])

    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vector_store = FAISS.from_documents(
	    documents=chunks,
	    embedding=embedding
    )

    return vector_store