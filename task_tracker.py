import os

TASK_FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    
    with open(TASK_FILE, 'r') as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {task}")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        completed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Completed task: {completed_task}")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted task: {deleted_task}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTask Tracker")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to complete: "))
            complete_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == '5':
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
