import AskGemini

conversation = []


def chat(user_message):
    conversation.append({"role": "user", "parts": [{"text": user_message}]})

    try:
        reply = AskGemini.ask_gemini(conversation)

    except Exception as e:
        return f"Sorry, somthing went worng: {e}"

    # conversation.append({"role":"user", "parts":[{"text": reply}]})
    return reply


print(chat("Hello, My name is rahul. Please remember it"))

print(chat("Whats my name?"))
