from abc import ABC, abstractmethod


# Абстрактний базовий клас для уявлень
class View(ABC):

    @abstractmethod
    def show_contact(self, contact):
        pass

    @abstractmethod
    def show_message(self, message):
        pass

    @abstractmethod
    def show_help(self):
        pass

    @abstractmethod
    def show_all_contacts(self, contacts):
        pass


class ConsoleView(View):

    def show_contact(self, contact):
        print(contact)

    def show_message(self, message):
        print(message)

    def show_help(self):
        print("You can:")
        print("add - add name and phone number;")
        print("close/exit - if you want quit;")
        print("change - if you need to do some change;")
        print("phone - you need enter name to see phone number")
        print("all - to see all list that you add")
        print("add-birthday - Add the date of birth for the specified contact.")
        print("show-birthday - Show the date of birth for the specified contact.")
        print("birthdays - Show upcoming birthdays within the next week.")

    def show_all_contacts(self, contacts):
        print(contacts)


def main():
    book = load_data()
    view = ConsoleView()
    view.show_message("Welcome to the assistant bot! Click the 'help' button to learn about all the commands.")
    while True:
        view.show_message("help/close/exit/add/change/phone/all/add-birthday/show-birthday/birthdays")
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            save_data(book)
            view.show_message("Good bye!")
            sys.exit(1)
        elif command == "hello":
            view.show_message("How can I help you? Please enter 'add' your name and number.")
        elif command == "help":
            view.show_help()
        elif command == "add":
            view.show_message(add_contact(args, book))
        elif command == "change":
            view.show_message(change_contact(args, book))
        elif command == "phone":
            view.show_message(show_phone(args, book))
        elif command == "all":
            view.show_all_contacts(book)
        elif command == "add-birthday":
            view.show_message(add_birthday(args, book))
        elif command == "show-birthday":
            view.show_message(show_birthday(args, book))
        elif command == "birthdays":
            view.show_message(birthdays(book))
        else:
            view.show_message("Unknown command. Please enter 'help' to see available commands.")

if __name__ == "__main__":
    main()


