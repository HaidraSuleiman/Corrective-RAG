from dotenv import load_dotenv

load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableSequence

class GradeAnswer(BaseModel):
    """
      Binary score determining whether the generated answer is good for the user question.
    """
    binary_score: bool = Field(
        description="Answer addresses the question, 'True' or 'False'"
    )

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
structured_llm_grader = llm.with_structured_output(GradeAnswer)

system = """You are a grader assessing whether an answer addresses / resolves a question \n
            Give a binary score 'yes' or 'no'. 'yes' means that the answer resolves /answers the question. """

answer_prompt = ChatPromptTemplate.from_messages(
    [
        {"role": "system", "content": system},
        {"role": "human", "content": "User question: \n\n {question} LLM generation: {generation}"}
    ]
)

answer_grader: RunnableSequence = answer_prompt | structured_llm_grader
