import os

def print_directory_contents(path):
    try:
        # List all the files and directories in the given path
        contents = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = '/home/zeeshan-khan/Desktop/python cource DOC'
print_directory_contents(directory_path)


