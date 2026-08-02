from task import Task
import json
from pathlib import Path

class Storage:
    
    def __init__(self, filename = "tasks.json"):
        self.path = Path(filename)

    def save(self,tasks: list[Task]):
        
        data = {
                    "tasks" : [task.to_dictionary() for task in tasks.tasks]
                }
        
        with self.path.open("w") as file:
            json.dump(data,file,indent=4)
            
            
    def load(self) -> list[Task]:
        
        if self.path.exists():
            with self.path.open() as file:
                data = json.load(file)

            return [
                Task.from_dictionary(task) 
                for task in data["tasks"]
            ]
        
        return None
                
                
        