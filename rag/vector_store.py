from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

def build_vector_store(incident_documents: list[str]):
    """
    Build an in-memory vector index for historical incidents.
    This allows semantic similarity search during RCA.
    """
    embedding_model = OllamaEmbeddings(model="llama3")
    return FAISS.from_texts(incident_documents, embedding_model)
