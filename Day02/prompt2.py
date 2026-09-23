import ollama
response = ollama.chat(
    model = "llama3.2:3b",
    messages = [
       {
        "role": "user",
        "content": " What is an AI?" 
       } 
    ]
)
print(response ["message"]["content"])