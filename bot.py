# Консольний бот-помічник з обробкою помилок через декоратор

def input_error(func):
    """
    Декоратор для обробки помилок у функціях команд.
    Обробляє KeyError, ValueError, IndexError.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Not enough arguments."
    return inner


# Словник для збереження контактів
contacts = {}


@input_error
def add_contact(args, contacts):
    """Додає контакт у словник"""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def show_phone(args, contacts):
    """Повертає номер телефону контакту"""
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts):
    """Повертає всі контакти"""
    if not contacts:
        return "No contacts found."
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    print("Welcome to your assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()
        
        if command == "exit":
            print("Goodbye!")
            break
        elif command.startswith("add"):
            parts = command.split()[1:]
            print(add_contact(parts, contacts))
        elif command.startswith("phone"):
            parts = command.split()[1:]
            print(show_phone(parts, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Unknown command. Available commands: add, phone, all, exit.")


if __name__ == "__main__":
    main()