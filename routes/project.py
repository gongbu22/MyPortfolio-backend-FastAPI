from fastapi import APIRouter
from models.project import Project
from schema.project import ProjectList
# from service.database import get_db

router = APIRouter()

@router.post("/details/{id}", response_model=ProjectList)
async def read_project(project: ProjectList):
    return await project(project)
