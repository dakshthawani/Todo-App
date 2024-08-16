fName = "todo.txt"


def get_todo(filename=fName):
    with open(filename, "r") as file_read:  # with block will close the file automatically
        todos_read = file_read.readlines()
        return todos_read


def write_todo(new_todos, filename=fName):
    with open(filename, "w") as file_read:
        file_read.writelines(new_todos)   # Writelines is used for list while write is used for string


if __name__ == "__main__":
    print(__name__)
    print(type(__name__))
    print("hello")
    print(get_todo())