# Topic of the Day: Building a CLI Menu (Project Skeleton)
# Explanation: Most beginner projects start as a "Command Line Interface" (CLI).
# You need a loop that keeps the program running until the user chooses to quit.

import sys


def show_menu():
    print("\n--- Student Manager 1.0 ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Exit")


def add_student():
    print(">> Feature: Add Student (Coming Soon)")


def view_students():
    print(">> Feature: View Students (Coming Soon)")


# The Main Application Loop
def main():
    while True:
        show_menu()
        choice = input("Enter choice (1-3): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Goodbye!")
            sys.exit()  # Clean exit
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()