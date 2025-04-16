from pydantic import BaseModel

class ProjectList(BaseModel):
    id: int
    name: str
    summary: str
    stack: str
    description: str