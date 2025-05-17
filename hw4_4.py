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

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone": # Print the phone number of a contact
            print(contacts.get(args[0]))
        elif command == "all":
            print("Contacts:")
            for name, phone in contacts.items(): # Print all contacts
                print(f"{name}: {phone}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()