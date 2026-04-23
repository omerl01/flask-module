from pydantic import BaseModel, Field
from bson.objectid import ObjectId

class Lists(BaseModel):
    name : str
    

class Tasks(BaseModel):
    title : str = Field(..., min_length=1)
    completed : bool = False
    list : str | None