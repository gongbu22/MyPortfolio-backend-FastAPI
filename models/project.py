from pydantic import BaseModel
from typing import Optional

class Project(BaseModel):
    id: int
    name: str
    summary: str
    stack: str
    description: str
    