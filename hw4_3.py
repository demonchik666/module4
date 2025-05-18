import sys
from pathlib import Path
from colorama import init, Fore
#Task 3
init(autoreset=True)

def print_directory_structure(path: Path, indent: str = ""):
    if not path.exists(): #Check if the path exists
        print(Fore.RED + f"Mistake: path '{path}' does not exist.")
        return
    if not path.is_dir(): #Check if the path is a directory
        print(Fore.RED + f"Mistake: path '{path}' is not a directory.")
        return

    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(indent + Fore.BLUE + f"📂 {item.name}")
            print_directory_structure(item, indent + " ┃ ")
        else:
            print(indent + Fore.GREEN + f"📜 {item.name}")

if __name__ == "__main__": 
    if len(sys.argv) != 2:
        directory_path = Path(input("Give me a path to a directory: "))
    else:
        directory_path = Path(sys.argv[1])
    print(Fore.CYAN + f"\nStructure of a directory: {directory_path}\n")
    print_directory_structure(directory_path) 
