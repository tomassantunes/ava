import logger

from llm import functions, system_messages
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

def transfer_to_read_file_agent():
    logger.log(logger.LogType.INFO, "Transfering to Read File Agent...")
    return read_file_agent

orchestrator = Agent(
    name="Orchestrator Agent",
    instructions=system_messages.get_orchestrator_context(),
    functions=[transfer_to_code_gen_agent, transfer_to_check_code_agent, transfer_to_create_file_agent, transfer_to_read_file_agent]
)

code_gen_agent = Agent(
    name="Code Generation Agent",
    instructions=system_messages.get_code_gen_context(),
    functions=[transfer_to_check_code_agent, functions.create_file_with_content]
)

check_code_agent = Agent(
    name="Check Code Agent",
    instructions=system_messages.get_check_code_context(),
    functions=[transfer_to_run_code_agent]
)

run_code_agent = Agent(
    name="Run Code Agent",
    instructions=system_messages.get_run_code_context(),
    functions=[functions.run_python_code]
)

test_code_agent = Agent(
    name="Test Code Agent",
    instructions="Test the code and return the results",
)

create_file_agent = Agent(
    name="Create File Agent",
    instructions=system_messages.get_create_file_context(),
    functions=[functions.create_file_with_content]
)

read_file_agent = Agent(
    name="Read File Agent",
    instructions=system_messages.get_read_file_context(),
    functions=[functions.read_file]
)