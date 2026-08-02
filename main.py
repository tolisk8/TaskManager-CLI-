from task import Task
from utils import clear_terminal
from task_manager import TaskManager
from cli import CLI
from storage import Storage

storage = Storage()

clear_terminal()
mytaskmanager = TaskManager() 
if storage.load():
    mytaskmanager = storage.load()        
cli = CLI(mytaskmanager)
cli.run()
storage.save(mytaskmanager)