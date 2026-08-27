from google import genai
from google.genai import types

client=genai.Client(
    api_key="GIVE YOUR API KEY"
)
user_prompt =input("Enter your prompt: ")
system_prompt = "limit your prompt in 1 sentence and 1 paragraph"
chat=client.chats.create(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
        system_instruction=system_prompt
    )
)



response=chat.send_message(user_prompt)
print(response.text)