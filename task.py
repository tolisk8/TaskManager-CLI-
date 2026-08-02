from enums import Priority,State


class Task:
    def __init__(self,taskname: str, description: str,priority:str,taskid: int = None,taskstate = 0):
            self.__taskid = taskid
            self.__name = taskname
            self.__description = description
            self.__priority = priority
            self.__state = taskstate    
        
    def to_dictionary(self):
        return {
            "id" : self.taskid,
            "name" : self.name, 
            "description" : self.description, 
            "priority" : self.__priority, 
            "state" : self.state 
        }

    @classmethod
    def from_dictionary(cls,data):
        return cls(data["name"],data["description"],int(data["priority"]),data["id"],int(data["state"]))
    
        
    @property
    def taskid(self):
        return self.__taskid
    @property
    def name(self):
            return self.__name 
    @property    
    def description(self):
            return self.__description 
    @property   
    def priority(self):
            return self.__priority 
    @property   
    def state(self):
            return self.__state 
    
    
    @taskid.setter
    def taskid(self, value:int):
        self.__taskid = value
    @name.setter
    def name(self,value: str):
        self.__name = value
    @description.setter
    def description(self,value: str):
            self.__description = value
    @priority.setter
    def priority(self,value: int):
            self.__priority = value
    @state.setter
    def state(self, state: int):
        self.__state = state