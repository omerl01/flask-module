from pydantic import BaseModel, Field


class Lists(BaseModel):
    name : str
    

class Tasks(BaseModel):
    title : str = Field(..., min_length=1)
    completed : bool = False
    list : str | None