from task_manager import TaskManager
from task import Task
from cli import CLI

def test_task():
    task = Task("Task1","My description",1)
    
    assert task.name == "Task1"
    
def test_manager():
    task1 = Task("Task1","My description",1)
    task2 = Task("Task1","My description",1)
    task3 = Task("Task1","My description",1)
    
    manager = TaskManager()
    
    manager.add_task(task1)
    manager.add_task(task2)
    manager.add_task(task3)
    
    assert len(manager) == 3
    

    


    
