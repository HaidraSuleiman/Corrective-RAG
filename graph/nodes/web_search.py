from typing import Any, Dict

from langchain_core.documents import Document
from langchain_tavily import TavilySearch

from graph.state import GraphState
from dotenv import load_dotenv

load_dotenv()

web_search_tool = TavilySearch(max_results=3)


def web_search(state: GraphState) -> Dict[str, Any]:
    print("---WEB SEARCH---")
    question = state["question"]
    documents = state["documents"] if "documents" in state else []

    #This has a key 'results' that holds a list of dictionaries each dictionary has a key content and url the answer is in content

    tavily_results = web_search_tool.invoke({"query": question}) 

    # We combine the 3 results into one langchain document 
    # 1. Join the content into one big string
    joined_tavily_result = "\n".join(      
        [tavily_result["content"] for tavily_result in tavily_results["results"]]
    )

    # 2. Create a document with the big string as page_content
    web_results = Document(page_content=joined_tavily_result)

    # We have the full state in this function and in previous steps of he graph we filtered the documents to keep only the relevant ones
    if documents is not None:
        documents.append(web_results)
    else: 
        documents = [web_results]

    return {"documents": documents, "question": question}


if __name__ == "__main__":
    web_search(state={"question": "agent memory", "documents": None})
    print()


    