import pickle


class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"{self.description} (Priority: {self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)

    def save_tasks(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self, file_name):
        with open(file_name, 'rb') as file:
            self.tasks = pickle.load(file)

def main():
    task_manager = TaskManager()

    while True:
        print("\n===== Task Manager =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority: ")
            task = Task(description, priority)
            task_manager.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            task_manager.show_tasks()
            if len(task_manager.tasks) == 0:
                continue
            task_index = int(input("Enter the index of the task to remove: "))
            if task_index >= 0 and task_index < len(task_manager.tasks):
                task_manager.remove_task(task_manager.tasks[task_index])
                print("Task removed successfully.")
            else:
                print("Invalid task index.")
        elif choice == "3":
            task_manager.show_tasks()
        elif choice == "4":
            file_name = input("Enter the file name to save tasks: ")
            task_manager.save_tasks(file_name)
            print("Tasks saved successfully.")
        elif choice == "5":
            file_name = input("Enter the file name to load tasks: ")
            task_manager.load_tasks(file_name)
            print("Tasks loaded successfully.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
