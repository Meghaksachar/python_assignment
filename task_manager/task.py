import json

# List to store tasks
tasks = []


class Task:
    """
    A class to represent a task.
    """

    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"


class TaskManager:
    """
    A class to manage tasks.
    """

    @staticmethod
    def add_a_task(title):
        """
        Add a new task to the task list.
        """
        task_id = len(tasks) + 1
        task = Task(task_id, title)
        tasks.append(task)

    @staticmethod
    def view_tasks():
        """
        View all tasks in the task list.
        """
        for task in tasks:
            print(task)

    @staticmethod
    def delete_a_task(task_id):
        """
        Delete a task from the task list by its ID.
        """
        global tasks
        tasks = [task for task in tasks if task.id != task_id]

    @staticmethod
    def mark_task_as_complete(task_id):
        """
        Mark a task as complete by its ID.
        """
        for task in tasks:
            if task.id == task_id:
                task.completed = True

    @staticmethod
    def save_tasks(filename='tasks.json'):
        """
        Save all tasks to a JSON file with indentation for better readability.
        """
        with open(filename, 'w') as file:
            json.dump([{
                'id': task.id,
                'title': task.title,
                'completed': task.completed
            } for task in tasks], file, indent=4)

    @staticmethod
    def load_tasks(filename='tasks.json'):
        """
        Load tasks from a JSON file.

        This function attempts to read tasks from the specified JSON file and parse them.
        """
        global tasks
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                tasks = [Task(**data) for data in tasks_data]
        except json.JSONDecodeError:
            print("Error: The JSON file is empty or not properly formatted.")
        except FileNotFoundError:
            print("Error: The JSON file was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to run the task manager.
    """
    task_manager = TaskManager()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save and Exit")
        choice = input("Choose an option (1 to 5): ")
        if choice == '1':
            title = input("Enter task title: ")
            task_manager.add_a_task(title)
            print("Added the task ",title)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_a_task(task_id)
            print("The task to be deleted is ",task_id," please press option 5 to save and exit the file")
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            task_manager.mark_task_as_complete(task_id)
        elif choice == '5':
            task_manager.save_tasks()
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    TaskManager.load_tasks()
    main()
