import logging
import logger

from llm import functions
from swarm import Agent


def transfer_to_code_gen_agent():
    logger.log(logger.LogType.INFO, "Transfering to Code Generation Agent...")
    return code_gen_agent

def transfer_to_run_code_agent():
    logger.log(logger.LogType.INFO, "Transfering to Run Code Agent...")
    return run_code_agent

def transfer_to_check_code_agent():
    logger.log(logger.LogType.INFO, "Transfering to Check Code Agent...")
    return check_code_agent

def transfer_to_create_file_agent():
    logger.log(logger.LogType.INFO, "Transfering to Create File Agent...")
    return create_file_agent

orchestrator = Agent(
    name="Orchestrator Agent",
    instructions="You are a helpful assistant that manages agents in order to satistfy the user queries. Transfer the user input to the correct agent. Example, if the use requests to run code, transfer to the Check Code Agent so this agent can check wheter the code is safe to run and then run it. If the user requests to generate code, transfer to the Code Generation Agent. If the user requests to save the code, transfer to the Create File Agent.",
    functions=[transfer_to_code_gen_agent, transfer_to_check_code_agent, transfer_to_create_file_agent]
)

code_gen_agent = Agent(
    name="Code Generation Agent",
    instructions="Generate code based on the user input and transfer to the Check Code Agent if the user requests for the code to be executed. If the user requests to save the code, use the crete_file_with_content function to create a file with the code.",
    functions=[transfer_to_check_code_agent, functions.create_file_with_content]
)

check_code_agent = Agent(
    name="Check Code Agent",
    instructions="Check whether the code is safe to run. If and only if the code is safe, transfer to the Run Code Agent.",
    functions=[transfer_to_run_code_agent]
)

run_code_agent = Agent(
    name="Run Code Agent",
    instructions="Run code and return the output",
    functions=[functions.run_python_code]
)

test_code_agent = Agent(
    name="Test Code Agent",
    instructions="Test the code and return the results",
)

create_file_agent = Agent(
    name="Create File Agent",
    instructions="Create a file with the given content",
    functions=[functions.create_file_with_content]
)