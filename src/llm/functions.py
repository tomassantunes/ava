import io
import utils
import logger

from contextlib import redirect_stderr, redirect_stdout


def run_python_code(code: str):
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()

    result = {
        'output': '',
        'errors': '',
        'success': True
    }

    try:
        logger.log(logger.LogType.INFO, "Running Python Code")
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            exec(code)

        result['output'] = stdout_capture.getvalue()
        result['errors'] = stderr_capture.getvalue()

    except Exception as e:
        result['errors'] = str(e)
        result['success'] = False
    
    finally:
        logger.log(logger.LogType.SUCCESS, "Python Code Ran Successfully")
        stdout_capture.close()
        stderr_capture.close()

    return result

def create_file_with_content(file_name: str, content: str):
    utils.create_scratchpad()

    try:
        with open(f"{utils.SCRATCPAD_DIR}/{file_name}", "w") as file:
            file.write(content)

        logger.log(logger.LogType.SUCCESS, f"File {file_name} created successfully")
    except Exception as e:
        logger.log(logger.LogType.ERROR, f"Error creating file: {e}")