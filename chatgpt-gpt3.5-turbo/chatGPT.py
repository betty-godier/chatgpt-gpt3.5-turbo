import os
import openai
openai.api_key = "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"

messages = [
    {"role": "system", "content" : "Hi Barbie!"}
]

content = input("User: ")
messages.append({"role": "user", "content": content})

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

chat_response = completion.choices[0].message.content 
print(f'ChatGPT: {chat_response}')