from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion     
from utility.phone import Phone



# zaimplementować funkcje obsługujące komendy np. add_phone()
# pamiętać o słowniku MAIN_COMMANDS z komendami


def add_phone():
    phone = input("Type phone or <<< if you want to cancel: ")
    if phone == "<<<":
        return None
    return Phone(phone)

MAIN_COMMANDS = {
    "new phone": add_phone,
}

#### powyższy fragment to przykład dla pamięci, w jaki sposób powinno działać



class CommandCompleter(Completer):
    def __init__(self, commands):
        self.commands = commands

    def get_completions(self, text, complete_event):
        word_before_cursor = text.get_word_before_cursor()
        matches = [] # lub krócej: matches = [cmd for cmd in self.commands if cmd.startswith(word_before_cursor)]
        for cmd in self.commands:
            if cmd.startswith(word_before_cursor):
                matches.append(cmd)
        
        for match in matches:
            yield Completion(match, start_position=-len(word_before_cursor))    # Wartość -len(word_before_cursor) oznacza, że podpowiedź zaczyna się na początku słowa przed kursorem.



def main():
    completer = CommandCompleter(MAIN_COMMANDS)
    user_input = prompt("Enter a command: ", completer=completer)   # completer=completer mówi funkcji prompt, żeby użyła CommandCompleter do obsługi autouzupełniania komend podczas wprowadzania danych przez użytkownika.

    if user_input in MAIN_COMMANDS: # Check if the command exists
        MAIN_COMMANDS[user_input]() # Calling the function assigned to a given command
        print("You entered:", user_input)
    else:
        print("Unknown command:", user_input)

if __name__ == "__main__":
    main()
   

