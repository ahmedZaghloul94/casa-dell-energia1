from pydantic import BaseModel
from typing import List, Optional
from typing import Optional


class Property(BaseModel):
    name: str
    value: str


class ResourceModel(BaseModel):
    name: str
    image: Optional[str] = None
    description: Optional[str] = None
    properties: Optional[List[Property]] = None
