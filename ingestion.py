from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
# Preparing resources
urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

# loading resources as langchain documents from urls

docs = [WebBaseLoader(url).load() for url in urls]  # list of langchain documents

docs_list = [item for sublist in docs for item in sublist]

# Preparing the text splitter
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250, chunk_overlap=0
)

# Performing the Chunking process using the text splitter
doc_splits = text_splitter.split_documents(docs_list)

print(f"splitted {len(docs_list)} langchain documents into {len(doc_splits)} chunks")

# Commneted this section out after running it once (Created the vector store and dont want to create it on every run)
####################################################################################################################

# Preparing the vector store Chroma with the documents the name of the store and embeddings model
# vectorstore = Chroma.from_documents(
#     documents=doc_splits,
#     collection_name="rag-chroma",
#     embedding=OpenAIEmbeddings(),
#     persist_directory="./.chroma",
    
# )
####################################################################################################################

# Creating a retriever to perform similarity searches and retrieve context
# Using as_retriever after Chroma object to turn it into a langchain retriever

retriever = Chroma(
    collection_name="rag-chroma",
    persist_directory="./.chroma",
    embedding_function=OpenAIEmbeddings(),
).as_retriever()

