from llm import comm

def main():
    print("Starting AVA...")
    user_input = input("Enter your message: ")
    response = comm.get_response(user_input)
    print("Response: " + response)
    
if __name__ == "__main__":
    main()