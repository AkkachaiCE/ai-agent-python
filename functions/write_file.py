import os

def main():
    print("Hello from write_file")

def write_file(working_directory, file_path, content):
    file_full_path = os.path.join(working_directory, file_path)

    file_full_path = os.path.abspath(file_full_path)
    working_directory = os.path.abspath(working_directory)

    if not file_full_path.startswith(working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    try:
        os.makedirs(os.path.dirname(file_full_path), exist_ok=True)
        with open(file_full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    main()