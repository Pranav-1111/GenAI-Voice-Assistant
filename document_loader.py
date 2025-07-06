from langchain.document_loaders import PyMuPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(file_paths):
    docs = []
    for path in file_paths:
        if path.endswith(".pdf"):
            loader = PyMuPDFLoader(path)
        else:
            loader = TextLoader(path)
        docs.extend(loader.load())
    return docs

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(docs)


