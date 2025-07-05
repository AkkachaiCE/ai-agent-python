import os
import subprocess

def main():
    print("Hello from run_python.py")

def run_python_file(working_directory, file_path):
    file_full_path = os.path.join(working_directory, file_path)

    file_full_path = os.path.abspath(file_full_path)
    working_directory = os.path.abspath(working_directory)

    if not file_full_path.startswith(working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(file_full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        results = subprocess.run(["uv", "run", file_full_path], 
                                cwd=working_directory, capture_output=True, timeout=30)
        outputs = []
        stdout_str = results.stdout.decode('utf-8').strip()
        stderr_str = results.stderr.decode('utf-8').strip()
        if results.stdout.strip():
            outputs.append(f"STDOUT:\n{stdout_str}")
        if results.stderr.strip():
            outputs.append(f"STDERR:\n{stderr_str}")
        if results.returncode != 0:
            outputs.append(f"Process exited with code {results.returncode}")
        if not outputs:
            return "No output produced."
        return "\n\n".join(outputs)
    
    except subprocess.TimeoutExpired:
        return "Error: Process timed out after 30 seconds."
    
    except Exception as e:
        return f"Error: executing Python file: {e}"

if __name__ == "__main__":
    main()