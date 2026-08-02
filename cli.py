from enums import Priority,State
from task import Task
from task_manager import TaskManager
from utils import clear_terminal
import time

class CLI:
    
    def __init__(self, manager: TaskManager):
        self.__manager = manager
        
    @property
    def manager(self):
        return self.__manager
    
    def add_task(self):
        print("...ADD A TASK...")
        name = input("Write the name of the Task: ")
        description = input("Write a description for a task: ")
        priority = int(input("Write the priority using numbers only (1.High, 2.Medium, 3.Low): "))
        
        task = Task(name,description,Priority(priority).value)
        self.manager.add_task(task)
        print("Task added correctly.")
        
    def modify_task(self):
        print("...EDIT A TASK...")
        id = int(input("Write the Id of the task to be edited: "))
        clear_terminal()
        print("...EDIT A TASK...")
        mytask = self.manager.get_task(id)
        if mytask is not None:
            print(f"Task to be edited: Name: {mytask.name}, Description: {mytask.description}, Priority: {Priority(mytask.priority).name}\n")
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
                    newdata = int(input(f"Priority:{Priority(mytask.priority).name}\nWrite the new priority using numbers only(1.High, 2.Medium, 3.Low): "))
                    mytask.priority = Priority(newdata).value
                case 4:
                    print("Canceling...")
                case _:
                    print("This option is not available, please choose one from the menu.")
            print("Task edited correctly.")
        else:
            print("The task was not found")
            
    
    def delete_task(self):
        print("...DELET A TASK...")
        id = int(input("Write the id of the task to be deleted: "))
        clear_terminal()
        print("...DELET A TASK...")
        if self.manager.delete_task(id):
            print("Tarea elimindada correctamente")
        else:
            print("Algo salió mal. Vuelve a intentarlo")
            
    def mark_completed(self):
        print("...MARK A TASK COMPLETED...")
        id = int(input("Write the id of the task to be marked as completed: "))
        if self.manager.task_completed(id):
            print("Task marked correctly correctly.")
        else:
            print("The task was not found.")
            
    def search_task(self):
        print("...SEARCH FOR A TASK...")
        option = int(input("Optoins:\n1.Search for ID\n2.Search for name or letter\n Select an option using numbers: "))
        clear_terminal()
        print("...SEARCH FOR A TASK...\n\n")
        print("   ------------------------    \n")
        
        match option:
            case 1:
                id = int(input("Write the ID for the task: "))
                task = self.manager.get_task(id)
                if task != None:
                    priority = Priority(task.priority)
                    state = State(task.state)
                    print(f"{task.taskid}. {task.name}\n Description:\n{task.description}\n\nPriority: {priority} State: {state}")
                else:
                    print("No task was found.")
            case 2:
                search = input("Write the name or words that match with the name of the task: ")
                print(f"Matches for {search}.\n")
                print("  ID  |    Name    ")
                if not self.manager.search_task(search):
                    print(f"No task was found using ('{search}')")
            case _:
                print("The option selected is not in the menu, try again.")
                
        input("Press enter to continue...")
        
        
    def welcome(self):
        print("=====================================")
        print("       Welcome to TaskManager        ")  
        print("=====================================")
        time.sleep(1)
        
    def menu(self):
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
    
    def run(self):
        self.welcome()
        key = True
        while key:
            clear_terminal()
            option = self.menu()
            match option:
                case 1: 
                    clear_terminal()
                    self.add_task()
                    time.sleep(1)
                case 2:
                    clear_terminal()
                    self.modify_task()
                    time.sleep(1)
                case 3:
                    clear_terminal()
                    self.delete_task()
                    time.sleep(1)
                case 4:
                    clear_terminal()
                    self.mark_completed()
                    time.sleep(1)
                case 5:
                    clear_terminal()
                    self.manager.show_tasks()
                    input("\n\nPress any key to go to menu... ")
                case 6:
                    clear_terminal()
                    self.search_task()
                    time.sleep(2)
                case 7:
                    print("Exiting....")
                    key = False
                    time.sleep(2)
                    clear_terminal()
                case _:
                    print("Sorry this option is not available.")
    
            