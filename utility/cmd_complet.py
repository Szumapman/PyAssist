import difflib
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion     



# metoda przykładowa użyta tylko do testów 
def add_phone(): 
    phone = input("Type phone or <<< if you want to cancel: ")
    if phone == "<<<":
        return None
    return phone

MAIN_COMMANDS = {
    "new phone": add_phone,
    "add phone": add_phone,
    "edit email": add_phone,
    "delete": add_phone,
    "show all": add_phone,
    "search": add_phone,
    "save": add_phone,
    "export": add_phone,
    "import": add_phone,
    "exit": add_phone,
}
#### powyższy fragment to przykład dla pamięci, w jaki sposób powinno działać



class CommandCompleter(Completer):
    def __init__(self, commands):
        self.commands = commands

    def get_completions(self, text, complete_event):
        word_before_cursor = text.get_word_before_cursor()
        matches = [cmd for cmd in self.commands if cmd.startswith(word_before_cursor)]
        if not matches:                                                                         # If no exact match was found
            close_matches = difflib.get_close_matches(word_before_cursor, self.commands.keys()) # Find the closest match
            if close_matches:                                                                   # If the closest match was found
                match = close_matches[0]
                yield Completion(match, start_position=-len(word_before_cursor))
            else:
                yield Completion(f"Unknown command: {word_before_cursor}")                      # If there is no exact and closest match
        else:
            for match in matches:                                                               # If the exact match was found
                yield Completion(match, start_position=-len(word_before_cursor))


def main():
    completer = CommandCompleter(MAIN_COMMANDS)
    user_input = prompt("Enter a command: ", completer=completer)                               # completer=completer tells the prompt function to use CommandCompleter to support autocomplete commands as the user enters data.

    if user_input in MAIN_COMMANDS:                                                             # Check if the command exists
        MAIN_COMMANDS[user_input]()                                                             # Calling the function assigned to a given command
        print("You entered:", user_input)
    else: 
        print(f"Unknown command, try again")

if __name__ == "__main__":
    main()
   

