import io
import os

from dotenv import load_dotenv
from openai import OpenAI
from swarm import Agent, Swarm
from contextlib import redirect_stderr, redirect_stdout

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = Swarm(client=OpenAI(api_key=api_key))

def run_python_code(code: str):
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()

    result = {
        'output': '',
        'errors': '',
        'success': True
    }

    try:
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            exec(code)

        result['output'] = stdout_capture.getvalue()
        result['errors'] = stderr_capture.getvalue()

    except Exception as e:
        result['errors'] = str(e)
        result['success'] = False
    
    finally:
        stdout_capture.close()
        stderr_capture.close()

    return result

def transfer_to_code_gen_agent():
    print("Transfering to Code Generation Agent...")
    return code_gen_agent

def transfer_to_run_code_agent():
    print("Transfering to Run Code Agent...")
    return run_code_agent

orchestrator = Agent(
    name="Orchestrator Agent",
    instructions="Orchestrates the other agents",
    functions=[transfer_to_code_gen_agent]
)

code_gen_agent = Agent(
    name="Code Generation Agent",
    instructions="Generate code from natural language and run the code using the Run Code Agent.",
    functions=[transfer_to_run_code_agent]
)

run_code_agent = Agent(
    name="Run Code Agent",
    instructions="Run code and return the output",
    functions=[run_python_code]
)

test_code_agent = Agent(
    name="Test Code Agent",
    instructions="Test the code and return the results",
)

def get_response(message: str):
    response = client.run(
        agent=orchestrator,
        messages=[{"role": "user", "content": message}]
    )
    
    return response.messages[-1]["content"]