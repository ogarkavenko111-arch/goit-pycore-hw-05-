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
        except Exception as e:
            return f"Unexpected error: {e}"
    return inner


# Словник для збереження контактів
contacts = {}


@input_error
def add_contact(args):
    """Додає контакт у словник"""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def show_phone(args):
    """Повертає номер телефону контакту"""
    name = args[0]
    return contacts[name]


@input_error
def show_all(args):
    """Повертає всі контакти"""
    if not contacts:
        return "No contacts found."
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

def parse_inut(user_input):
    parts = user_input.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def main():
    print("Welcome to your assistant bot!")
    
    commands = {
        "add": add_contact,
        "phone": show_phone,
        "all": show_all
    }
    
    
    while True:
        user_input = input("Enter a command: ").strip()
        
        if not user_input:
            continue
        
        command, args = parse_inut(user_input)
        
        if command in ["exit", "close"]:
            print("Goodbye!")
            break
        
        func = commands.get(command)
        
        if func:
            print(func(args))
        else:
            print("Unknown command. Available commands: add, phone, all, exit.")


if __name__ == "__main__":
    main()