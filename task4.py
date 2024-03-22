def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return "Give me name and phone please."
        except KeyError as e:
            return "Contact not found."
        except IndexError as e:
            return "Please enter both name and phone."

    return inner

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Please enter both name and phone.")
    name, phone = args
    if name in contacts:
        raise KeyError("Contact already exists.")
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Please enter both name and new phone.")
    name, phone = args
    if name not in contacts:
        raise KeyError("Contact not found.")
    contacts[name] = phone
    return "Contact successfully updated."

@input_error
def show_contact(args, contacts):
    if len(args) != 1:
        raise ValueError("Please enter the contact's name.")
    name = args[0]
    if name not in contacts:
        raise KeyError("Contact not found.")
    return contacts[name]

@input_error
def show_all(contacts):
    if not contacts:
        raise ValueError("Contact list is empty.")
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        raise ValueError("No data entered")
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

def main():
    contacts = {}
    print("Welcome to the assistant!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)
            if command in ["close", "exit"]:
                print("Goodbye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_contact(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                print("Invalid command.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
