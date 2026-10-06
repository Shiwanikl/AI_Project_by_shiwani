import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("no api found")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"

# Pydantic model
class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema = Ticket.model_json_schema()

response_format = {
    "type": "json_object"
}

system_prompt = f"""
Extract information from the customer ticket strictly based on this schema.
Return only valid JSON.

Schema:
{schema}
"""

message_system = {
    "role": "system",
    "content": system_prompt
}

text = """hi my name is shiwani, i bought this phone last year and it is not working.
this is my mail jkkjh@gmail.com, my contact no 8977"""

prompt = f"""
This is a customer ticket.
Extract the name, email, and issue.

Customer ticket:
{text}
"""

message_user = {
    "role": "user",
    "content": prompt
}

messages = [message_system, message_user]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format
)

answer = response.choices[0].message.content

print(answer)

import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)
print(ticket.name)
print(ticket.email)
print(ticket.issue)