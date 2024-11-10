from llm import comm

def main():
    print("Starting AVA...")
    messages: list[dict] = []
    while True:
        user_input = input("Enter your message: ")
        messages.append({"role": "user", "content": user_input})

        response = comm.get_response(messages)
        print("Response: " + response)

        messages.append({"role": "assistant", "content": response})
    
if __name__ == "__main__":
    main()