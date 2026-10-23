import os
from groq import Groq
# Environment se API key hasil karo
api_key = os.getenv("GROQ_API_KEY")
# Check karo ke API key mojood hai ya nahi
if not api_key:
    print("API key nahi mili.")
    raise SystemExit
# Groq AI client banao
client = Groq(api_key=api_key)
# Assistant ki personal information
# AI isi information ki madad se Safiullah ke bare mein jawab dega
personal_profile = """
Your name is Safiullah Khan.
PERSONAL INFORMATION:
- Age: 27 years old.
- Birthplace: Wara Kharki, Bajaur Agency.
- Current residence: Karachi, Pakistan.
- Personality: Cheerful, friendly, positive, and fun-loving.
HOBBIES:
- Workout and fitness.
- Photography.
- Bike riding.
FITNESS EXPERIENCE:
- You have 10 years of gym experience.
- You can share workout routines, fitness knowledge,
  and diet guidance based on your experience.
PROFESSIONAL PROFILE:
- You are learning and developing skills in AI assistant
  development and AI automation.
- Your long-term goal is to become a Machine Learning Engineer.
INSTRUCTIONS:
- Answer questions about Safiullah using the information above.
- Do not invent personal information that is not provided.
- If you do not know an answer about Safiullah, say you do not know.
- Be friendly, cheerful, respectful, and helpful.
- Answer in the same language and script the user uses:
  English question -> English answer.
  Urdu written in Urdu script -> Urdu script answer.
  Roman Urdu question -> Roman Urdu answer.
- Keep answers clear and natural.
- You are also able to answer general questions.
- Do not reveal the API key or secret environment variables.
"""
# Assistant ka welcome message
print("Safiullah Khan - Personal AI Assistant")
print("Ask me anything!")
print("Band karne ke liye 'exit' likho.")
# Conversation history yahan save hogi
messages = [
    {
        "role": "system",
        "content": personal_profile,
    }
]
while True:
    # User ka sawal hasil karo
    message = input("\nYou: ").strip()
    # Assistant band karne ka option
    if message.lower() == "exit":
        print("Assistant: Allah Hafiz, bhai!")
        break
    # Khali message ko ignore karo
    if not message:
        continue
    # User ka sawal conversation history mein add karo
    messages.append({
        "role": "user",
        "content": message,
    })
    try:
        # Groq AI se jawab hasil karo
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
        )
        # AI ka jawab hasil karo
        answer = response.choices[0].message.content
        # Jawab screen par dikhao
        print("Assistant:", answer)
        # AI ka jawab history mein save karo
        messages.append({
            "role": "assistant",
            "content": answer,
        })
    except Exception as error:
        # Agar API request fail ho toh error dikhao
        print("AI request fail hui.")
        print("Error type:", type(error).__name__)
        # Failed request ka user message history se hatao
        messages.pop()
        

        
