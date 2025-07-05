import os

def main():
    get_files_info()

def get_files_info(working_directory, directory=None):
    full_path = os.path.join(working_directory, directory)

    full_path = os.path.abspath(full_path)
    working_directory = os.path.abspath(working_directory)

    if not full_path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    try:
        files = []
        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)
            is_dir = os.path.isdir(item_path)
            file_size = os.path.getsize(item_path)
            files.append(f"- {item}: file_size:{file_size} bytes, is_dir={is_dir}")
        return "\n".join(files)
    except Exception as e:
        return f"Error listing files: {e}"

if __name__ == "__main__":
    main()