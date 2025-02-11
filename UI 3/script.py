import os

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}' successfully.")
    except FileNotFoundError:
        print(f"Result:The file '{old_name}' changed to '{new_name}'.")
    except FileExistsError:
        print(f"Result: A file '{new_name}' is changed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome to the File Rename CLI")
    old_name = input("Enter the current name of the file: ")
    new_name = input("Enter the new name for the file: ")
    rename_file(old_name, new_name)

if __name__ == "__main__":
    main()
