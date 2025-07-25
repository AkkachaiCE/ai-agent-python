from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def main():
    # print(get_files_info("calculator", "."))
    # print("================================")
    # print(get_files_info("calculator", "pkg"))
    # print("================================")
    # print(get_files_info("calculator", "/bin"))
    # print("================================")
    # print(get_files_info("calculator", "../"))

    # print(get_file_content("calculator", "lorem.txt"))
    # print("================================")

    # print(get_file_content("calculator", "main.py"))
    # print("================================")
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print("================================")
    # print(get_file_content("calculator", "/bin/cat"))
    # print("================================")

    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print("================================")
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print("================================")
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    # print("================================")

    print(run_python_file("calculator", "main.py"))
    print("================================")
    print(run_python_file("calculator", "tests.py"))
    print("================================")
    print(run_python_file("calculator", "../main.py"))
    print("================================")
    print(run_python_file("calculator", "nonexistent.py"))
    print("================================")


if __name__ == "__main__":
    main()