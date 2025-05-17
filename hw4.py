import sys
from pathlib import Path
from colorama import init, Fore

#Task 1
def total_salary(path):
    total = 0
    workers_count = 0
    try: #Check if the file exists
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                parts = line.split(',')
                if len(parts) != 2: #Check if the line has 2 parts
                    print(f'Invalid data in line: {line}, Reason: Incorrect number of parts')
                    continue
                numbers = parts[1]
                try: #Check if the salary is a number
                    numbers = float(numbers)
                except ValueError:
                    print(f'Invalid data in line: {line}, Reason: Not a number')
                    continue
                if numbers < 0: #Check if the salary is negative
                    print(f'Invalid data in line: {line}, Reason: Negative salary')
                    continue
                total += numbers
                workers_count += 1
    except FileNotFoundError:
        print(f'File {path} not found.')
        return (0, 0)
    if workers_count == 0: #Check if there are any valid lines
        print('No valid data found.')
        return (0, 0)
    return (total, total / workers_count)

# result = total_salary('workers.txt')
# if(result != (0, 0)):
#     total, average = result
#     print(f'Total salary: {total}\nAverage salary: {average}')

#Task 2
def get_cats_info(path):
    result = []
    try: #Check if the file exists
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                parts = line.split(',')
                if len(parts) != 3: #Check if the line has 3 parts
                    print(f'Invalid data in line: {line}, Reason: Incorrect number of parts')
                    continue
                if not parts[2].isdigit(): #Check if the age is a number
                    print(f'Invalid data in line: {line}, Reason: Age is not a number')
                    continue
                cat = {'id': parts[0], 'name': parts[1], 'age': parts[2]}
                result.append(cat)
    except FileNotFoundError:
        print(f'File {path} not found.')
        return []
    if not result: #Check if there are any valid lines
        print('No valid data found.')
    return result

# cats_info = get_cats_info("cats.txt")
# for cat in cats_info:
#     print(cat)

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

# if __name__ == "__main__": 
#     if len(sys.argv) != 2:
#         sys.exit(1)
#     directory_path = Path(sys.argv[1])
#     print(Fore.CYAN + f"\nStructure of a directory: {directory_path}\n")
#     print_directory_structure(directory_path)