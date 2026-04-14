from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Tell Me About sky in just 10 words"
)

print(response.output_text)
# import os
# print(os.getenv("OPENAI_API_KEY"))