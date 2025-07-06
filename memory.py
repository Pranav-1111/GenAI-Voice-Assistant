from sentence_transformers import SentenceTransformer
import faiss
import pickle
import os

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.IndexFlatL2(384)
store = []

# Load memory if exists
if os.path.exists("memory_store.pkl") and os.path.exists("memory_index.index"):
    with open("memory_store.pkl", "rb") as f:
        store = pickle.load(f)
    index = faiss.read_index("memory_index.index")

def remember(text):
    embedding = model.encode([text])
    index.add(embedding)
    store.append(text)
    
    # Save to disk
    with open("memory_store.pkl", "wb") as f:
        pickle.dump(store, f)
    faiss.write_index(index, "memory_index.index")

def retrieve(query, top_k=1):
    if len(store) == 0:
        return "Memory is empty."
    
    embedding = model.encode([query])
    D, I = index.search(embedding, top_k)
    return store[I[0][0]]
