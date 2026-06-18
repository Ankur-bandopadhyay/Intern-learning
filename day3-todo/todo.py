import os,json
import sys

TASK_FILE="tasks.json"

def load_tasks():

    # Read tasks from tasks.json.Returns an empty list if the file doesnt exist

    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE,"r") as f:
        return json.load(f)
    

def save_tasks(tasks):
    # write the current list of tasks back to tasks.json
    with open(TASK_FILE,"w") as f:
        json.dump(tasks,f,indent=2)    

def add_task(tasks,description):
    # Add a new task and persist it immediately
    tasks.append(description)
    save_tasks(tasks)
    print(f"added a task:{description}")

def remove_task(tasks,number):
    # remove a task by its 1-based position
    index= number-1

    if index <0 or index > len(tasks):
        print(f"there is no tasked numbered {number}")
        return
    removed=tasks.pop(index)
    save_tasks(tasks)
    print(f"removed task:{removed}")    

def list_tasks(tasks):
    # print the current tasks 
    if not tasks:
        print("no tasks yet .Add one")
        return
    
    for i,task in enumerate(tasks,start=1):
        print(f"{i}.{task}")

def main():
    args =sys.argv[1:]

    if not args:
        print("USAGE: python todo.py <add|remove|list> [argument]")
        return
    
    command=args[0]
    tasks=load_tasks()

    if command == "add":
        if len(args) < 2:
            print("Error:please provide a task description.Example: python todo.py add \"buy milk\"")
            return
        description= " ".join(args[1:])

        add_task(tasks,description)

    elif command =="remove":
        if len(args) <2:
            print("Error: please provide a task number to remove. Example: python todo.py remove 1") 
            return
        
        try:
            number= int(args[1])
        except ValueError:
            print(f"Error: '{args[1]}'is not a valid task number")

            return
        remove_task(tasks,number) 

    elif command == "list":
        list_tasks(tasks)

    else:
        print(f"Unknown command: {command}. Use add,remove,or list.")

if __name__ == "__main__":
    main()           