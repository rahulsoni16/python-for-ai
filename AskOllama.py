import ollama


def ask_ollama(prompt_text):
    try:
        # Calls the local Ollama instance running llama3.2
        response = ollama.chat(
            model='llama3.2.1',
            messages=[
                {
                    'role': 'user',
                    'content': prompt_text,
                },
            ],
        )
        
        # Extract and return the text content from the response
        return response['message']['content']
        
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    prompt = "Explain quantum computing in simple terms."
    print(f"Prompt: {prompt}\n")
    
    answer = ask_ollama(prompt)
    print(f"Ollama Response:\n{answer}")