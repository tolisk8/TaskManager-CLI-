import os
import time
class Task:
    def __init__(self,TaskName: str, Description: str,Priority:str,TaskId = None):
            self.taskid = TaskId
            self.name = TaskName
            self.description = Description
            self.priority = Priority
            self.state = 0


class TaskManager:
    def __init__(self):
        self.tasks = []
            
    def addTask(self,task: Task):
        if len(self.tasks) != 0:
            id = self.tasks[-1].taskid
            task.taskid = id
            self.tasks.append(task)
        else:
            task.taskid = 1
            self.tasks.append(task)
        
        
    def showTasks(self):
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
            
            
    def deleteTask(self,id):
        i = id - 1
        self.tasks.pop(i)
        print("Tarea eliminada correctamente")
    
    def taskCompleted(self,id):
        i = id - 1
        task = self.tasks[i]
        task.state = 1
    
        
def clearTerminal():
    os.system("cls")
                
        
def welcome():
    print("=====================================")
    print("       Welcome to TaskManager        ")  
    print("=====================================")
    time.sleep(1)
    
    



def AddTask(taskmanager):
    print("...ADD A TASK...")
    name = input("Write the name of the Task: ")
    description = input("Write a description for a task: ")
    priority = input("Write the priority using numbers only (1.High, 2.Medium, 3.Low): ")
    newtask = Task(name,description,priority)
    taskmanager.addTask(newtask)
    print("Task added correctly.")
    
    
    
def ModifyTask(taskmanager):
    print("...EDIT A TASK...")
    id = int(input("Write the Id of the task to be edited."))
    clearTerminal()
    print("...EDIT A TASK...")
    i = id - 1
    mytask = taskmanager.tasks[i]
    if mytask.priority == 1:
        priority = "High"
    elif mytask.priority == 2:
        priority = "Medium"
    else:
        priority = "Low"
    print(f"Task to be edited: Name:{mytask.name}, Description:{mytask.description}, Priority{priority}\n")
    print("       -----------------------------------------------------------           \n")
    option = int(input("1.Name\n2.Description\n3.Priority\n4.Cancel\nChoose an option from the menu using the numbers:")) 
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
            
    
        
def DeleteTask(taskmanager):
    print("...DELET A TASK...")
    id = int(input("Write the id of the task to be deleted: "))
    clearTerminal()
    print("...DELET A TASK...")
    i = id - 1
    confirm = input(f"Are you sure you want to delete ({taskmanager.tasks[i].name})? use y/n to yes or no")
    if confirm == "y":
        taskmanager.deleteTask(id)
        print("Task deleted correctly.")
    else:
        print("Operation canceled.")
    

def MarkCompleted(taskmanager):
    print("...MARK A TASK COMPLETED...")
    id = int(input("Write the id of the task to be marked as completed: "))
    i = id - 1
    taskmanager.taskCompleted(id)
    print("Task marked correctly correctly.")

def menu():
    print("TASK MANAGER")
    print("1.Add a Task") 
    print("2.Modify a Task")
    print("3.Delete a Task")        
    print("4.Mark as completed")
    print("5.Show all Tasks")
    print("6.Exit")
    option = int(input("Choose an option from the menu using the numbers: "))
    return option





def main(mytaskmanager: TaskManager):
    welcome()
    key = True
    while key:
        clearTerminal()
        option = menu()
        match option:
            case 1: 
                clearTerminal()
                AddTask(mytaskmanager)
                time.sleep(1)
            case 2:
                clearTerminal()
                ModifyTask(mytaskmanager)
                time.sleep(1)
            case 3:
                clearTerminal()
                DeleteTask(mytaskmanager)
                time.sleep(1)
            case 4:
                clearTerminal()
                MarkCompleted(mytaskmanager)
                time.sleep(1)
            case 5:
                clearTerminal()
                mytaskmanager.showTasks()
                input("\n\nPress any key to go to menu... ")
            case 6:
                print("Exiting....")
                key = False
                time.sleep(2)
                clearTerminal()
            case _:
                print("Sorry this option is not available.")
        
        
clearTerminal()
mytaskmanager = TaskManager()              
main(mytaskmanager)