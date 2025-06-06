#Task 4
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts: # Check if the contact exists
        contacts[name] = new_phone
        return "Contact changed."
    else:
        return "Contact not found."
    
def phone_number(args, contacts):
    if args[0] in contacts: # Check if the contact exists
        return contacts[args[0]]
    else:
        return "Contact not found."

def print_all(contacts):
    if len(contacts) == 0: # Check if there are any contacts
        return "No contacts found."
    else:
        result = "Contacts: \n"
        for name, phone in contacts.items(): # Print all contacts
            result += f"{name}: {phone}\n"
        return result
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]: # Exit the program
            print("Good bye!")
            break
        elif command == "hello": # Greet the user
            print("How can I help you?")
        elif command == "add": # Add a contact
            print(add_contact(args, contacts))
        elif command == "change": # Change a contact
            print(change_contact(args, contacts))
        elif command == "phone": # Print the phone number of a contact
            print(phone_number(args, contacts))
        elif command == "all": # Print all contacts
            print(print_all(contacts))  
        else: # Invalid command
            print("Invalid command.")

if __name__ == "__main__":
    main()
