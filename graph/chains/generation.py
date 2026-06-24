# from langchain_hub import hub
# from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

# prompt = hub.pull("rlm/rag-prompt")

# generation_chain = prompt | llm | StrOutputParser()

# print("generation.py loaded")
# print(dir())
 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("human", """You are an assistant for question-answering tasks. \
Use the following pieces of retrieved context to answer the question. \
If you don't know the answer, just say that you don't know. \
Use three sentences maximum and keep the answer concise.
 
Question: {question}
Context: {context}
Answer:""")
])

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)


generation_chain = prompt | llm | StrOutputParser()