import ollama
print("My AI Q&A Bot")
print("Type exit to Stop.\n")
while True:
    question=input("You:" )
    if question.lower()=="exit":
        print("Bot: Goodbye!")
        break
    
    response=ollama.chat(
        model="llama3.2",
        messages=[
            {
            "role":"user",
            "content":prompt
            }
        ]
    )
    print("Bot:",response["message"]["content"])

