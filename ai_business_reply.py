import os  # Environment variables access karne ke liye

from groq import Groq  # Groq AI se connect hone ke liye

# API key environment se hasil karo

api_key = os.getenv("GROQ_API_KEY")

# Check karo ke API key mili hai ya nahi

if not api_key:

    print("GROQ_API_KEY nahi mili. Pehle API key set karo.")

    raise SystemExit

# Groq AI client banao

client = Groq(api_key=api_key)

# Business ka naam input lo

business_name = input("Business ka naam: ")

# Customer ka message input lo

customer_message = input("Customer ka message: ")

# AI ko request bhejo

response = client.chat.completions.create(

    model="openai/gpt-oss-20b",

    messages=[

        {

            "role": "system",

            "content": (

                "You are a professional business customer support assistant. "

                "Write polite, helpful and concise replies. "

                "Never invent prices, policies or promises. "

                "Reply in the same language as the customer. "

                "If the price is unknown, politely say that it needs confirmation."

            ),

        },

        {

            "role": "user",

            "content": (

                f"Business name: {business_name}\n"

                f"Customer message: {customer_message}\n"

                "Write a suitable reply to the customer."

            ),

        },

    ],

)

# AI ka jawab hasil karo

ai_reply = response.choices[0].message.content

# Result screen par dikhao

print("\n" + "=" * 40)

print("BUSINESS:", business_name)

print("=" * 40)

print("\nAI GENERATED REPLY:\n")

print(ai_reply)

print("\n" + "=" * 40)
