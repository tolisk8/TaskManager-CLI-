from task import Task
from enums import Priority,State
from utils import clear_terminal




class TaskManager:
    
    """Manages the creation, storage and retrieval of tasks"""
    

    
    
    def __init__(self):
        self.__tasks = []
        
        
    @property
    def tasks(self):
        return self.__tasks
            
    def add_task(self,task: Task):
        
        """Adds a task to the manager"""
        
        if len(self.tasks) == 0:
            id = 1
        else:
            id = self.tasks[-1].taskid + 1
        
        task.taskid = id
        self.tasks.append(task)
        
        
        
    def show_tasks(self):
        
        """Returns all the tasks created"""
        
        tasks = []

        for task in self.tasks:
            tasks.append(task)
        return tasks
        
            
    def delete_task(self,id: int):
        
        """Deletes a task using it`s id"""
        
        for task in self.tasks:
            if id == task.taskid:
                self.tasks.pop(self.tasks.index(task))
                return True
        
        return False
    
    
        
    
    def task_completed(self, id: int):
        
        """Marks the state for the task as completed"""
        
        task = self.get_task(id)
        if task is not None:
            task.state = 1
            return True
        else:
            return False
                
                
    def get_task(self,id: int):
        
        """Returns a task for the Id given"""
        
        for task in self.tasks:
            if task.taskid == id:
                return task
        return None    
    
    def search_task(self,value: str):
        
        """returns the tasks that were found using some value"""
        
        list1 = []
        for task in self.__tasks:
            if value.lower() in task.name.lower():
                list1.append(task)
        
        if len(list1) == 0:
            return False
        
        return list1   
        

    
    
    
    
    

                
        

        


    



        
        





