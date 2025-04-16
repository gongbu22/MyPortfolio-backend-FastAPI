from fastapi import APIRouter, HTTPException
from models.project import Project
from schema.project import ProjectList
# from service.database import add_project, get_projects, get_project_by_id
from bson.objectid import ObjectId


router = APIRouter()


# 임시 데이터
fake_db = [
    {
        "id": 1,
        "name": "Project 1",
        "summary": "Summary of project 1",
        "stack": "Python, FastAPI",
        "description": "Description of project 1"
    },
    {
        "id": 2,
        "name": "Project 2",
        "summary": "Summary of project 2",
        "stack": "Node.js, MongoDB",
        "description": "Description of project 2"
    },
    {
        "id": 3,
        "name": "Project 1",
        "summary": "Summary of project 1",
        "stack": "Python, FastAPI",
        "description": "Description of project 1"
    },
    {
        "id": 4,
        "name": "Project 2",
        "summary": "Summary of project 2",
        "stack": "Node.js, MongoDB",
        "description": "Description of project 2"
    },
]

@router.get("/projects", response_model=list[ProjectList])
async def get_projects():

    return fake_db

# # 모든 프로젝트 조회
# @router.get("/projects/")
# async def fetch_projects():
#     projects = await get_projects()
#     return projects

# # 특정 프로젝트 조회
# @router.get("/projects/{project_id}")
# async def fetch_project(project_id: str):
#     project = await get_project_by_id(project_id)
#     if project is None:
#         raise HTTPException(status_code=404, detail="Project not found")
#     return project