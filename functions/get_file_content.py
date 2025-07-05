import os

def main():
    print("Hello from get_file_content.py")

def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000
    file_full_path = os.path.join(working_directory, file_path)

    file_full_path = os.path.abspath(file_full_path)
    working_directory = os.path.abspath(working_directory)

    if not file_full_path.startswith(working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(file_full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(file_full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        return file_content_string
    except Exception as e:
        return f'Error: {e}'
if __name__ == "__main__":
    main()