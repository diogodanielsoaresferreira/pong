from enum import Enum

class Events(Enum):
    CREATE = "create"
    CREATED = "created"
    JOIN = "join"
    JOINED = "joined"
    ERROR = "error"
    STATE = "state"
