from document_loader import load_documents, split_documents
from sentence_transformers import SentenceTransformer
import faiss
import pickle
import os

model = SentenceTransformer("all-MiniLM-L6-v2")
doc_store = []
doc_index = faiss.IndexFlatL2(384)

# Load saved document memory if available
if os.path.exists("doc_chunks.pkl") and os.path.exists("doc_index.index"):
    with open("doc_chunks.pkl", "rb") as f:
        doc_store = pickle.load(f)
    doc_index = faiss.read_index("doc_index.index")

def index_documents(file_paths):
    global doc_store, doc_index

    docs = load_documents(file_paths)
    chunks = split_documents(docs)
    texts = [chunk.page_content for chunk in chunks]

    embeddings = model.encode(texts)
    doc_index.add(embeddings)
    doc_store.extend(texts)

    # Save
    with open("doc_chunks.pkl", "wb") as f:
        pickle.dump(doc_store, f)
    faiss.write_index(doc_index, "doc_index.index")

def query_documents(query, top_k=1):
    if not doc_store:
        return "No documents indexed yet."

    embedding = model.encode([query])
    D, I = doc_index.search(embedding, top_k)
    return "\n".join([doc_store[i] for i in I[0]])
