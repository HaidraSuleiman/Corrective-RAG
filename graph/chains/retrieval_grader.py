from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

# The shape of the structured output that we want the LLM to output
class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents"""

    binary_score: str = Field(
        description="Documents are relevant to the question, 'yes' or 'no'"
    )

# Hooking it up to the LLM
structured_llm_grader = llm.with_structured_output(GradeDocuments)

# Preparing the prompts
system = """You are a grader assessing relevance of a retrieved document to a user question. \n
        If the document contains keyword(s) or semantic meaning relevant to the question, grade it as relevant. \n
        Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.
    """

grade_prompt = ChatPromptTemplate.from_messages(
    [
        {
            "role": "system", "content": system
        },
        {"role": "human", "content": "Retrieved document: \n\n {documents}  \n\n User question: {question}"}
    ]
)

# Assembling the Chain
retrieval_grader = grade_prompt | structured_llm_grader