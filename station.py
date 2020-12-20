from pydantic import BaseModel
from typing import List, Optional
from position import Position
#from resource import Resource


class Station(BaseModel):
    name: str
    address: Optional[list] = None
    position: Position
    image: Optional[str] = None
    description: Optional[str] = None
    #resoureces: Optional[List[Resource]] = None
