from dotenv import load_dotenv

from graph.graph import app

load_dotenv()


if __name__ == "__main__":
    print("Hello from corrective-rag!")
    result = app.invoke(input={"question": "how to make pizza?"})
    print(result['generation'])