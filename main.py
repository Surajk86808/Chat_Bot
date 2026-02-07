from dotenv import load_dotenv
from crew import stock_crew


load_dotenv()

def run(stock: str):
    result = stock_crew.kickoff(inputs={"stock": stock})
    print("#" * 280)
    print(result)
    print("#" * 280)


if __name__ == "__main__":
    run("TESLA")
   