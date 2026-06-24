from dotenv import load_dotenv

from graph.graph import app

load_dotenv()


if __name__ == "__main__":
    print("Hello from corrective-rag!")
    result = app.invoke(input={"question": "what is agent memory?"})
    print(result['generation'])