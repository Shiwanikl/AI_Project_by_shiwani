import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("no api found")

client=Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"
role="user"
prompt1="hi"
prompt2="explain time travel in detail"
prompt3="write a 1000 word essay on machinelearning"
prompts =[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={ 
    "role":"system",
    
    "content": "You are my strict tech manager and act accordingly professional behaviour"
}
    messages=[message]
    response = client.chat.completions.create(model=model,messages=messages)
    usage=response.usage
    print(f"Prompt: {prompt} --> your tokens: {usage.prompt_tokens} completion tokens: {usage.completion_tokens} total tokens: {usage.total_tokens}")
#message={
 #   "role": role,
  #  "content": prompt
#}
#messages=[message_system ,message]
#response = client.chat.completions.create(
 #   model=model,
  #  messages=messages,
    #temp we add as a parameter in response range is 0 to 2
   # temperature=0
#)
#print(response)
#print("###################")

#answer = response.choices[0].message.content
#print(answer)
