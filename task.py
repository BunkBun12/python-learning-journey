print("==== Task Manager ====")

print("""1.Add Task
2.View Task
3.Complete Task
4.Delete Task
5.Exit
""")

tasks = []

def add_task():
  name = input("Enter the tittle/name of task :")
  subject = input("Enter the subject :")
  task_summary = input("enter the task :")

  new_task = {
    "name" : name,
    "subject" : subject,
    "task_summary" : task_summary,
    "status" :  False
  }

  tasks.append(new_task)

def view_task():
  print(f"The active tasks are :")
  for task in tasks:
    print(task)
    if task["status"]:
      print("[✅]")
    else:
      print("[❎]")

def complete_task():
  print("select the task to mark complete:")
  for task in tasks:
    print(task)

  choice = input("enter the title/name :")
  for task in tasks:
    if choice == task["name"]:
      print(f"Completed: {task['name']}")
      task["status"] = True

def delete_task():
  choice = input("enter the name to delete the task:")

  for task in tasks:
    if choice == task["name"]:
       tasks.remove(task)
  
choice = None

while choice != 5:
  choice = int(input("enter (1 - 5) :"))

  match choice :
    case 1:
      add_task()

    case 2:
      view_task()

    case 3 :
      complete_task()

    case 4:
      delete_task()

    case 5:
      print("Exiting .......")

    case _:
      print("Invalid Input")