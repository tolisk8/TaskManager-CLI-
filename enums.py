from enum import Enum

class State(Enum):
    PENDING = 0
    COMPLETED = 1
    
class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3