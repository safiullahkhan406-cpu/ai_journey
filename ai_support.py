import os
from groq import Groq

# Environment se API key hasil karo
api_key = os.getenv("GROQ_API_KEY")

# API key check karo
if not api_key:
    print("API key nahi mili.")
    raise SystemExit

# Groq client banao
client = Groq(api_key=api_key)

# Assistant ka welcome message
print("AI Customer Support Assistant")
print("Band karne ke liye 'exit' likho.")

while True:
    # Customer ka message lo
    message = input("\nYou: ").strip()

    # Exit karne ka option
    if message.lower() == "exit":
        print("Assistant: Allah Hafiz, bhai!")
        break

    # Khali message ignore karo
    if not message:
        continue

    try:
        # AI se jawab hasil karo
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful customer support assistant. "
                        "Give polite, clear, and short answers."
                    ),
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )

        # AI ka jawab print karo
        answer = response.choices[0].message.content
        print("Assistant:", answer)

    except Exception as error:
        print("AI request fail hui.")
        print("Error type:", type(error).__name__)
        
