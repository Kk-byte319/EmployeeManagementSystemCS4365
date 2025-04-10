import openai

openai.api_key = "INSERT KEY HERE - NOT INCLUDED IN REPO FOR SECURITY REASONS"

def ai_chat():
    print("AI Chatbot is ready! Type 'exit' to quit.")
    conversation = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        conversation.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # or "gpt-3.5-turbo" for cheaper option
                messages=conversation
            )

            reply = response['choices'][0]['message']['content']
            print("AI:", reply)

            conversation.append({"role": "assistant", "content": reply})

        except Exception as e:
            print("Something went wrong:", e)

if __name__ == "__main__":
    ai_chat()




