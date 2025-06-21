import os
from subprocess import run
from subprocess import CalledProcessError, STDOUT ,TimeoutExpired
def run_python_file(working_directory, file_path):
    if not file_path:
        return 
    abs_working_directory = os.path.abspath(working_directory);
    full_file_path = f'{abs_working_directory}/{file_path}';
    is_file_exists = os.path.exists(full_file_path)
    if not is_file_exists:
        raise Exception(f'Error: File "{file_path}" not found.')
    list_of_content = os.listdir(abs_working_directory)
    if file_path not in list_of_content:
        raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    file_extension = list(file_path.split('.'))[-1]
    if file_extension != 'py':
        raise Exception(f'Error: "{file_path}" is not a Python file.')
    
    try:
        output = run(["python3",full_file_path],timeout=30, check=True, text=True, stderr=STDOUT)
        if output:
            return f'STDOUT: {output}'
        return "No output produced"
    except CalledProcessError as callProcessError:
        raise Exception(f'Process exited with code {callProcessError.returncode}')
    except TimeoutExpired as timeExpired:
        raise Exception(f'STDERR: {timeExpired.stderr}')
    except PermissionError as pe:
        raise Exception(pe)
    except Exception as e:
        raise Exception(f'STDERR: {e}')
        
    
    