import openai
import os

os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.environ["OPENAI_API_KEY"]

def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    message = response.choices[0].text
    return message.strip()

prompt = "What is the meaning of life?"


keep_prompting=True
while keep_prompting:
    prompt=input("What's Your question ??\n")
    if prompt == 'exit':
      keep_prompting =False
    else:
      response = ask_gpt(prompt)
      print(response)