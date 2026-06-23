from dotenv import load_dotenv

load_dotenv()

from graph.chains.retrieval_grader import GradeDocuments, retrieval_grader
from ingestion import retriever



def test_retrieval_grader_answer_yes() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {"question": question, "documents": doc_txt}
    )
    assert res.binary_score == "yes"

def test_retrieval_grader_answer_no() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {"question": "how to make pizza", "documents": doc_txt}
    )
    assert res.binary_score == "no"