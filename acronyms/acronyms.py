WORKFILE = "C:/Users/leeuw582/OneDrive - KPN BV/Desktop/P3c/acronyms/my_files/acronyms.txt"

def find_acronym():
    look_up = input("Enter the acronym you want to look up:\n")
    found = False
    try:
        with open(WORKFILE, 'r') as file:
            for line in file:
                if look_up.upper() in line.upper():
                    print(line)
                    found = True
                    break
    except FileNotFoundError:
        print("Error: The file was not found.")
        return
    
    if not found:
        print("Acronym not found in the file.")

def add_acronym():
    acronym = input("Enter an acronym: ")
    definition = input("Enter the definition: ")

    with open(WORKFILE, 'a') as file:
        file.write(f"{acronym.upper()} - {definition}\n")
        
def main():
    while True:
        action = input("Would you like to (1) look up an acronym or (2) add a new acronym? (Enter 'exit' to quit): ")
        if action == '1':
            find_acronym()
        elif action == '2':
            add_acronym()
        elif action.lower() == 'exit' or action.lower() == 'quit':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 'exit'.")
            
main()