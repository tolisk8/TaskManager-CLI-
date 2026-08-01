import os
import time
import json
from pathlib import Path
from enum import Enum

class State(Enum):
    PENDING = 0
    COMPLETED = 1
    
class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class Task:
    def __init__(self,taskname: str, description: str,priority:str,taskid: int = None,taskstate = 0):
            self.taskid = taskid
            self.name = taskname
            self.description = description
            self.priority = priority
            self.state = taskstate
            
    def to_dictionary(self):
        return {
            "id" : self.taskid,
            "name" : self.name, 
            "description" : self.description, 
            "priority" : self.priority, 
            "state" : self.state 
        }

    @classmethod
    def from_dictionary(cls,data):
        return cls(data["name"],data["description"],int(data["priority"]),int(data["id"]),int(data["state"]))

class TaskManager:
    def __init__(self):
        self.tasks = []
            
    def add_task(self,task: Task):
        
        if len(self.tasks) == 0:
            task.taskid = 1
        else:
            pastid = self.tasks[-1].taskid 
            id = pastid + 1
            task.taskid = id
        
        self.tasks.append(task)
        
        
        
    def show_tasks(self):
        print("  ID  |     Name     |    Priority    |   State   ")
        for task in self.tasks:
            if task.state == 0:
                state = "Pending"
            else: 
                state = "Completed"
            if task.priority == 1:
                priority = "High"
            elif task.priority == 2:
                priority = "Medium"
            else:
                priority = "low"
            print(f"  {task.taskid}        {task.name}          {priority}         {state}")
            
            
    def delete_task(self,id):
        self.tasks.pop(id)
        print("Tarea eliminada correctamente")
    
    def task_completed(self,id):
        task = self.tasks[id]
        task.state = 1
        
    def get_task(self,id):
        for task in self.tasks:
            if task.taskid == id:
                return task
        return None
    
    
    
    
        
def clear_terminal():
    os.system("cls")
                
        
def welcome():
    print("=====================================")
    print("       Welcome to TaskManager        ")  
    print("=====================================")
    time.sleep(1)
    

    



def add_task(taskmanager):
    print("...ADD A TASK...")
    name = input("Write the name of the Task: ")
    description = input("Write a description for a task: ")
    priority = input("Write the priority using numbers only (1.High, 2.Medium, 3.Low): ")
    newtask = Task(name,description,priority)
    taskmanager.addTask(newtask)
    print("Task added correctly.")
    
    
    
    
    
def modify_task(taskmanager):
    print("...EDIT A TASK...")
    id = int(input("Write the Id of the task to be edited: "))
    clear_terminal()
    print("...EDIT A TASK...")
    mytask = taskmanager.getId(id)
    if mytask != None:
        if mytask.priority == 1:
            priority = "High"
        elif mytask.priority == 2:
            priority = "Medium"
        else:
            priority = "Low"
        print(f"Task to be edited: Name: {mytask.name}, Description: {mytask.description}, Priority: {priority}\n")
        print("       -----------------------------------------------------------           \n")
        option = int(input("1.Name\n2.Description\n3.Priority\n4.Cancel\nChoose an option from the menu using the numbers: ")) 
        match option:
            case 1:
                newdata = input(f"Name:{mytask.name}\nWrite the new name: ")
                mytask.name = newdata
            case 2:
                newdata = input(f"Description:{mytask.description}\nWrite the new description: ")
                mytask.description = newdata
            case 3:
                newdata = int(input(f"Priority:{priority}\nWrite the new priority using numbers only(1.High, 2.Medium, 3.Low): "))
                mytask.priority = newdata
            case 4:
                print("Canceling...")
            case _:
                print("This option is not available, please choose one from the menu.")
        print("Task edited correctly.")
    else:
        print("The task was not found")
            
    
        
def delete_task(taskmanager):
    print("...DELET A TASK...")
    id = int(input("Write the id of the task to be deleted: "))
    clear_terminal()
    print("...DELET A TASK...")
    task = taskmanager.getId(id)
    if task != None:
        confirm = input(f"Are you sure you want to delete ({task.name})? use y/n to yes or no: ")
        if confirm == "y":
            taskmanager.deleteTask(taskmanager.tasks.index(task))
            print("Task deleted correctly.")
        else:
            print("Operation canceled.")
    else: 
        print("Task not found.")
    
def mark_completed(taskmanager):
    print("...MARK A TASK COMPLETED...")
    id = int(input("Write the id of the task to be marked as completed: "))
    task = taskmanager.getId(id)
    if task != None:
        taskmanager.taskCompleted(taskmanager.tasks.index(task))
        print("Task marked correctly correctly.")
    else:
        print("The task was not found.")

def search_task(taskmanager):
    print("...SEARCH FOR A TASK...")
    option = int(input("Optoins:\n1.Search for ID\n2.Search for name or letter\n Select an option using numbers: "))
    clear_terminal()
    print("...SEARCH FOR A TASK...\n\n")
    print("   ------------------------    \n")
    
    match option:
        case 1:
            id = int(input("Write the ID for the task: "))
            task = taskmanager.getId(id)
            if task != None:
                match task.priority:
                    case 1:
                        priority = "High"
                    case 2:
                        priority = "Medium"
                    case 3: priority = "Low"
                if task.state == 1:
                    state = "Completed"
                else:
                    state = "Pending"
                print(f"{task.taskid}. {task.name}\n Description:\n{task.description}\n\nPriority: {priority} State: {state}")
            else:
                print("No task was found.")
        case 2:
            search = input("Write the name or wordsd that match with the name of the task: ")
            mylist = []
            print(f"Matches for {search}.\n")
            print("  ID  |    Name    ")
            for task in taskmanager.tasks:
                if search.lower() in task.name.lower():
                    print(f" {task.taskid}          {task.name}")
                    mylist.append(task)
            if len(mylist) == 0:
                print(f"No tasks where found using {search}")
        case _:
            print("The option selected is not in the menu, try again.")
            
    input("Press enter to continue...")
        


def menu():
    print("TASK MANAGER")
    print("1.Add a Task") 
    print("2.Modify a Task")
    print("3.Delete a Task")        
    print("4.Mark as completed")
    print("5.Show all Tasks")
    print("6.Search a task")
    print("7.Exit")
    option = int(input("Choose an option from the menu using the numbers: "))
    return option


def write_json(mytaskmanager):
    data = {
        "tasks" : [task.toDictionary() for task in mytaskmanager.tasks]
    }

    with open("tasks.json", "w") as file:
        json.dump(data,file,indent=4)


def read_json(mytaskmanager):
    file_path = Path("tasks.json")
    
    if file_path.exists():
        with open("tasks.json","r") as file:
                data = json.load(file)
                mytaskmanager.tasks = [Task.from_dict(task) for task in data["tasks"]]
    
    
    

def main(mytaskmanager: TaskManager):
    read_json(mytaskmanager)
    welcome()
    key = True
    while key:
        clear_terminal()
        option = menu()
        match option:
            case 1: 
                clear_terminal()
                add_task(mytaskmanager)
                time.sleep(1)
            case 2:
                clear_terminal()
                modify_task(mytaskmanager)
                time.sleep(1)
            case 3:
                clear_terminal()
                delete_task(mytaskmanager)
                time.sleep(1)
            case 4:
                clear_terminal()
                mark_completed(mytaskmanager)
                time.sleep(1)
            case 5:
                clear_terminal()
                mytaskmanager.show_tasks()
                input("\n\nPress any key to go to menu... ")
            case 6:
                clear_terminal()
                search_task(mytaskmanager)
                time.sleep(2)
            case 7:
                print("Exiting....")
                key = False
                time.sleep(2)
                clear_terminal()
            case _:
                print("Sorry this option is not available.")
        write_json(mytaskmanager)
    
        
        
clear_terminal()
mytaskmanager = TaskManager()              
main(mytaskmanager)



