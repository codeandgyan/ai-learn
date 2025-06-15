# Retrieval-Augmented Generation
RAG is an AI technique that combines the power of information '*retrieval*' with large language models (*LLMs*) to enhance the '*accuracy*' and '*context-awareness*' of AI-generated responses.

# RAG Steps
## Data Ingestion Process
- Chunking:- Break the data into chunks
- Embeddings:- Create Vector Embeddings of each chunk and attach metadata to each each chunk
- Store the Embeddings in Vector Store (DB)
 *Indexing*

## Data Retrieval Process
- User Query
- Create Embeddings of the User Query
- Search the embeddings based on similarity score from Vector DB
- Search returns *relevant chunks*
- Filter the relevant chunk from the data in my data source
- Pass the relevant chunk to the LLM along with user query

# Simple RAG Chain implementation approach
loader = pdf_loader(path)
splitter = text_splitter()
embedding = OpenAI() or Gemini()
qdrant = Qdrant_vector()

> Langchain Expression Language (LCEL)

chain = loader | splitter | embedding | qdrant

chain.invoke(pdf_path);

# To run the RAG application
## Setup the Vector Store (Qdrant DB)
- Run the docker container by running this command `docker compose -f docker-compose.db.yml up`
- The Qdrant DB comes with a web-based dashboard as well http://localhost:6333/dashboard