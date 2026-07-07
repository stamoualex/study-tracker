import json
import os

def load_assignments():
    previous_data = os.path.exists("assignments.json")
    if previous_data:  
        with open("assignments.json") as file:
            data = json.load(file)
            print("Assignments loaded succesfully")
            return data
    else: 
        return []

def save_assignments(): 
    with open("assignments.json", "w") as file:
        json.dump(assignment_database, file)





assignment_database = load_assignments()


def view_assignment():
    if not assignment_database:
        print("No assignments yet")
    else:
        for assignment in assignment_database:
            print(assignment)


def add_assignment():
    new_assignment = input("Enter an assignment: ")
    assignment_database.append(new_assignment)
    print(f"Added: {new_assignment}")


def assignment_remove():
    if not assignment_database:
        print("No assignments yet")
        return

    remove_assignment = input("Which assignment would you like to remove: ")
    if remove_assignment in assignment_database:
        assignment_database.remove(remove_assignment)
        print(f"Removed: {remove_assignment} ")
    else:
        print(f"Could not find {remove_assignment}")


def categorizing():
    if user_choice == 1:
        view_assignment()
        show_menu = input("Enter yes when you are ready to continue: ")
        while show_menu != "yes":
            show_menu = input("Please enter yes when you are ready to continue: ")
        exit = "no"
        return exit
    elif user_choice == 2:
        add_assignment()
        show_menu = input("Enter yes when you are ready to continue: ")
        while show_menu != "yes":
            show_menu = input("Please enter yes when you are ready to continue: ")
        save_assignments()
        exit = "no"
        return exit
    elif user_choice == 3:
        if not assignment_database:
            print("No assignments yet")
        else:
            view_assignment()
            assignment_remove()
        show_menu = input("Enter yes when you are ready to continue: ")
        while show_menu != "yes":
            show_menu = input("Please enter yes when you are ready to continue: ")
        save_assignments()
        exit = "no"
        return exit
    elif user_choice == 4:
        print("You have exited succesfully!")
        exit = "yes"
        return exit
    else:
        print("Please enter a valid number (1-4): ")
        exit = "no"
        return exit


def menu():
    print("*****************")
    print("This is an interactive menu.")
    print("1. View assignments")
    print("2. Add assignment")
    print("3. Remove assignment")
    print("4. Exit")
    print("*****************")
    user_choice = int(input("Choose an option (1-4): "))
    return user_choice


exit = "no"
while exit == "no":
    user_choice = menu()
    exit = categorizing()







