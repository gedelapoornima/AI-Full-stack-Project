import ollama
response = ollama.chat(
    model = "llama3.2:3b",
    messages = [
       {
        "role": "user",
        "content": "what is an AI?Give the main types of AI with one line definations." 
       } 
    ]
)
print(response ["message"]["content"])