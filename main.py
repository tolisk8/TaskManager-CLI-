from task import Task
from utils import clear_terminal
from task_manager import TaskManager
from cli import CLI
from storage import Storage


def main():
    storage = Storage()

    clear_terminal()
    mytaskmanager = TaskManager()
    mylist = storage.load()   
        
    if len(mylist) != 0:
        for task in mylist:
            mytaskmanager.add_task(task)
        
    cli = CLI(mytaskmanager)
    cli.run()
    storage.save(mytaskmanager)
    
if __name__ == "__main__":
    main()


