import os 
from pathlib import Path

MAX_CHARS = 10000
def write_file(working_directory, file_path=None, content=None):
    if not file_path:
        raise Exception(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory') 
    # working_abs_path = os.path.abspath(working_directory)
    # full_path = f'{working_directory}/{file_path}' 
    # abs_path = os.path.abspath(full_path)
    if file_path.startswith("/"):
      raise Exception(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    full_file_path_str = f'{working_directory}/{file_path}'
    p = Path(full_file_path_str)
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)  
        characters = p.read_text()
        return (f'Successfully wrote to "{file_path}" ({len(characters)} characters written)') 
    except Exception as e:
        raise Exception(f'Error: {e}')
