from dotenv import load_dotenv
import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(api_key)

# Provide the file path which is pdf
pdf_path = Path(__file__).parent / "Python Programming.pdf"

# Initialize the PDF Loader with the pdf file path
loader = PyPDFLoader(file_path=pdf_path)

# Load the document
docs = loader.load()

# Create a text splitter to split the documents into small chunks
# Chunk size can be computed based on our requirement, hardcoding it for the time-being, we can also specify some overlap
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# Split the document into different chunks
split_docs = text_splitter.split_documents(documents=docs)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", google_api_key=api_key
)

# # Ingestion stage--------
# vector_store = QdrantVectorStore.from_documents(
#     documents=[],
#     url="http://localhost:6333",
#     collection_name="python-guide-book",
#     embedding=embeddings,
# )

# vector_store.add_documents(documents=split_docs)

# print("Ingestion Done")

## Retrieval stage--------
retriever = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="python-guide-book",
    embedding=embeddings,
)

relevant_chunks = retriever.similarity_search(
    query="What are the types of operators in python?"
)

print("Relevant Chunks", relevant_chunks)

SYSTEM_PROMPT = f"""
You are a helpful AI Assistant who responds based on the available context pulled from a PDF document.
Return references to the context such as Page number, page label, title or anything you deem relevant within the response.

# Context:
{relevant_chunks}
"""

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=api_key,
)

query = input("Enter your query: ")

messages = [
    (
        "system",
        SYSTEM_PROMPT,
    ),
    ("human", query),
]
response = llm.invoke(messages)
print("🤖 Response:", response.text)
