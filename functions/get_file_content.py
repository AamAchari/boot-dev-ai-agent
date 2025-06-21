import os 

MAX_CHARS = 10000
def get_file_content(working_directory, file_path=None):
    if not file_path:
        return 
    working_abs_path = os.path.abspath(working_directory)
    full_path = f'{working_directory}/{file_path}' 
    abs_path = os.path.abspath(full_path)
    print(abs_path)
    is_dir = os.path.isdir(abs_path)
    is_file = os.path.isfile(abs_path)
    if not is_file:
        if len(file_path) > 0:
            sub_paths = file_path.split("/")
            file_name_to_be = sub_paths[-1]
            working_directory_content = os.listdir(working_abs_path)
            for sub_path in sub_paths[:-1]:
                if sub_path not in working_directory_content:
                    raise Exception(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        raise Exception(f'Error: File not found or is not a regular file: "{file_path}"')
    try:
        with open(abs_path, 'r') as file:
            file_content_as_string = file.read(MAX_CHARS)
            return file_content_as_string
    except Exception as e:
        raise Exception(e)
   
    