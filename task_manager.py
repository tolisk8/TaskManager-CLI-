from task import Task
from enums import Priority,State
from utils import clear_terminal

class TaskManager:
    def __init__(self):
        self.__tasks = []
        
    @property
    def tasks(self):
        return self.__tasks
            
    def add_task(self,task: Task):
        if len(self.tasks) == 0:
            id = 1
        else:
            id = self.tasks[-1].taskid + 1
        
        task.taskid = id
        self.tasks.append(task)
        
        
        
    def show_tasks(self):
        print("  ID  |     Name     |    Priority    |   State   ")
        for task in self.tasks:
            print(f"  {task.taskid}        {task.name}          {Priority(task.priority).name}         {State(task.state).name}")
            
            
    def delete_task(self,id):
        for task in self.tasks:
            if id == task.taskid:
                self.tasks.pop(self.tasks.index(task))
                return True
        
        return False
    
    
        
    
    def task_completed(self, id):
        task = self.get_task(id)
        if task is not None:
            task.state = 1
            return True
        else:
            return False
                
                
    def get_task(self,id):
        for task in self.tasks:
            if task.taskid == id:
                return task
        return None    
    
    def search_task(self,value):
        list1 = []
        for task in self.__tasks:
            if value.lower() in task.name.lower():
                print(f" {task.taskid}          {task.name}")
                list1.append(task)
        
        if len(list1) == 0:
            return False
        
        return True    
        

    
    
    
    
    

                
        

        


    



        
        





