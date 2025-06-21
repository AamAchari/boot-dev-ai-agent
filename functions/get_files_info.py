import os 

error = False
def get_files_info(working_directory, directory=None):
    if not directory:
        return
    relative_path = f'{working_directory}/{directory}'
    abs_relative_path = os.path.abspath(relative_path)
    if not os.path.isdir(abs_relative_path):
        error=True
        # print(abs_relative_path)
        raise Exception(f'Error: "{directory}" is not a directory')
    if directory != '.' and directory not in os.listdir(working_directory):
        error=True
        raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    # print("abs_relative_path: " + abs_relative_path)
    
    s = f'- {directory}: file_size={os.path.getsize(abs_relative_path)}, is_dir={os.path.isdir(abs_relative_path)}\n'
    result = [s]
    for content in os.listdir(relative_path):
        temp_relative_path = f'{relative_path}/{content}'
        temp_abs_path = os.path.abspath(temp_relative_path)
        # print("content: " + content)
        # print("content temp_path: " + temp_abs_path)
        if os.path.isdir(temp_abs_path):
            result.append(get_files_info(relative_path, content))
            # s = f"- {content}: file_size={os.path.getsize(content)}, is_dir=True"
        else:
            s = f'- {content}: file_size={os.path.getsize(temp_abs_path)}, is_dir={os.path.isdir(temp_abs_path)}\n'
            result.append(s)
    return ''.join(result)