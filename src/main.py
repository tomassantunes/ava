from llm import agents

def main():
    print("Starting AVA...")
    code = agents.get_response("Generate hello world in python.")
    print(code)
    
if __name__ == "__main__":
    main()