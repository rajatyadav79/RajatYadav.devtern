import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation?",
  temperature=0.9,
  max_tokens=300,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
