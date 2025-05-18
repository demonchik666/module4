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
