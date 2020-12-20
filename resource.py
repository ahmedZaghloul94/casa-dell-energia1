from pydantic import BaseModel
from typing import List, Optional
#from resource_model import ResourceModel
from station import Station
from position import Position
#from rent import Rent
import json

class ResourceParameter(BaseModel):
    name: str
    value: str


class Resource(BaseModel):
    name: str
    position: Position
    parameters: Optional[List[ResourceParameter]]
    image:str
    state: str

