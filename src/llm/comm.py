import os

from dotenv import load_dotenv
from openai import OpenAI
from swarm import Swarm
from llm import agents

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
swarm = Swarm(client=client)

def get_completion(prompt: str, system: str, model: str = "gpt-4o-mini"):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content

def get_response(messages: list[dict], context_vars: dict = {}):
    response = swarm.run(
        agent=agents.orchestrator,
        messages=messages,
        context_variables=context_vars
    )
    
    return response.messages[-1]["content"]