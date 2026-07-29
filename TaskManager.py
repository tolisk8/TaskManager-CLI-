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
        for task in self.tasks:
            if task.state == 0:
                state = "Pending"
            else: 
                state = "Completed"
            print(task.taskid,task.name,state,sep="-",end="")
            print(" -> ", end="")
            
    def deleteTask(self,id):
        i = id - 1
        self.tasks.pop(i)
        print("Tarea eliminada correctamente")
    
    def taskCompleted(self,id):
        i = id - 1
        task = self.tasks[i]
        task.state = 1
    
        
       
                
        
def welcome():
    print("=====================================")
    print("       Welcome to TaskManager        ")  
    print("=====================================")



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
    id = input("Write the Id of the task to be edited.")
    i = id - 1
    mytask = taskmanager[i]
    option = int(input("1.Name\n2.Description\n3.Priority\n4.Cancel\nChoose an option from the menu using the numbers:")) 
    match option:
        case 1:
            newdata = input("Write the new name: ")
            mytask.name = newdata
        case 2:
            newdata = input("Write the new description: ")
            mytask.description = newdata
        case 3:
            newdata = int(input("Write the new priority using numbers only(1.High, 2.Medium, 3.Low): "))
            mytask.priority = newdata
        case 4:
            print("Canceling...")
        case _:
            print("This option is not available, please choose one from the menu.")
            
    
        
def DeleteTask(taskmanager):
    print("...DELET A TASK...")
    id = int(input("Write the id of the task to be deleted: "))
    i = id - 1
    taskmanager.deleteTask(id)
    print("Task deleted correctly.")

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

def clearTerminal():
    os.system("cls")

def main(key):
    welcome()
    clearTerminal()
    option = menu()
    match option:
        case 1: 
            clearTerminal()
            AddTask(mytaskmanager)
            time.sleep(2)
        case 2:
            clearTerminal()
            ModifyTask(mytaskmanager)
            time.sleep(2)
        case 3:
            clearTerminal()
            DeleteTask(mytaskmanager)
            time.sleep(2)
        case 4:
            clearTerminal()
            MarkCompleted(mytaskmanager)
            time.sleep(2)
        case 5:
            clearTerminal()
            mytaskmanager.showTasks()
            input("Press any key to go to menu... ")
        case 6:
            print("Exiting....")
            key = False
            time.sleep(5)
        case _:
            print("Sorry this option is not available.")
        
        
        
mytaskmanager = TaskManager()              
key = True
while key:
    main(key)