import os
 
FILE_NAME = "tasks.txt"
 
 
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                status, text = line.split("|", 1)
                tasks.append({"text": text, "done": status == "1"})
    return tasks

def save_tasks(tasks):
     with open(FILE_NAME, "w") as f:
        for task in tasks:
            status = "1" if task["done"] else "0"
            f.write(f"{status}|{task['text']}\n")

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")
 
 
def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['text']}")
 
 
def add_task(tasks):
    text = input("Enter the new task: ").strip()
    if text:
        tasks.append({"text": text, "done": False})
        save_tasks(tasks)
        print("Task added!")
    else:
        print("Task can't be empty.")
 
 
def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number.")
 
 
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['text']}")
    except (ValueError, IndexError):
        print("Invalid task number.")
 
 
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
 
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
 
 
if __name__ == "__main__":
    main()
           