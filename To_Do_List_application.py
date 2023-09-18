
# This code defines a Python class named TodoList. This class is used to create a to-do list object.
class TodoList:
    # Inside the __init__ method, an instance of the class is initialized.
    def __init__(self):
        # It contains an empty list named self.tasks that will be used to store the tasks.
        self.tasks = []

    # The add_task method is used to add a task to the to-do list.
    # It takes two arguments: self (which refers to the instance of the class) and task (the task to be added).
    def add_task(self, task):
        self.tasks.append(task)
        # The method appends the task to the self.tasks list and prints a message confirming that the task was added.
        print(f"Task '{task}' added.")

    # The remove_task method is used to remove a task from the to-do list.
    # It takes two arguments: self (the instance of the class) and task (the task to be removed).
    def remove_task(self, task):
        # The method checks if task is in the self.tasks list. If it is, it removes the task from the list and prints a message confirming the removal. 
        # If the task is not found, it prints a message indicating that the task was not found in the list.
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found in the list.")

    # The display_tasks method is used to display the tasks in the to-do list.
    # It takes only self as an argument (the instance of the class).
    def display_tasks(self):
        # The method checks if there are any tasks in the self.tasks list. If the list is empty, it prints a message indicating that there are no
        #  tasks. If there are tasks, it prints each task along with its index.
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

# The main function is the entry point of the program.
def main():
    # Inside main, an instance of the TodoList class is created, which initializes an empty to-do list.
    todo_list = TodoList()

    # The program enters a loop that continues until the user chooses to quit (choice == "4").
    # It displays a menu with options for adding, removing, displaying tasks, or quitting the program.
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")

        # The program prompts the user to enter their choice by inputting a number corresponding to the menu options.
        choice = input("Enter your choice: ")

        # If the user chooses option "1," they are prompted to enter a task, and the add_task method is called to add the task to the to-do list.
        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        # If the user chooses option "2," they are prompted to enter a task to remove, and the remove_task method is called to remove the task from the list.
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        # If the user chooses option "3," the display_tasks method is called to display the current tasks in the list.
        elif choice == "3":
            todo_list.display_tasks()
        # If the user enters an invalid choice (a number other than 1, 2, 3, or 4), an error message is displayed, and the menu is shown again.
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

#  the code checks if the script is being run directly (not imported as a module), and if so, it calls the main function to start the program.
if __name__ == "__main__":
    main()
