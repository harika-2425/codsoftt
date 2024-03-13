tasks = []
def addTask():
  task = input("Please enter a task: ")
  tasks.append(task)
  print(f"Task '{task}' added to the list.")

def updateTask():
    listTasks()  # Display the current tasks
    if not tasks:
        print("There are no tasks to update.")
        return

    try:
        task_index = int(input("Enter the index of the task you want to update: "))
        if 0 <= task_index < len(tasks):
            new_task = input("Enter the updated task description: ")
            tasks[task_index] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")
#List of the Tasks
def listTasks():
  if not tasks:
    print("There are no tasks currently.")
  else:
    print("Current Tasks:")
    for index, task in enumerate(tasks):
      
      print(f"Task #{index}. {task}")

if __name__ == "__main__":
  ### Create a loop to run the app
  print("Welcome to the to do list app :)")
  while True:
    print("\n")
    print("Please select one of the following options")
    print("------------------------------------------")
    print("1. Add a new task")
    print("2. Update a task")
    print("3. List of the tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if (choice == "1"):
      addTask()
    elif (choice == "2"):
      updateTask()
    elif (choice == "3"):
      listTasks()
    elif (choice == "4"):
      break
    else:
      print("Invalid choice")