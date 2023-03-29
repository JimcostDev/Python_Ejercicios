"""
    1. Instalar openai:
        pip install openai
"""
import openai
openai.api_key = "key"

while True:
    try:
        prompt = input("\n Introduce una pregunta: ")
        if prompt == "exit":
            break

        completion = openai.Completion.create(engine="text-davinci-003",
                                prompt= prompt,
                                max_tokens=2048)

        print(completion.choices[0].text)
    except openai.error.RateLimitError as err:
        print(err)
