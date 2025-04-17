from fastapi import APIRouter, HTTPException
from models.project import Project
from schema.project import ProjectList
# from service.database import add_project, get_projects, get_project_by_id
from bson.objectid import ObjectId
from service.database import db
from dotenv import load_dotenv
import os

# 환경변수 로드
load_dotenv()

MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")

router = APIRouter()


def serialize_project(project) -> dict:
    project["_id"] = str(project["_id"])
    return project

@router.get("/")
async def root():
    collections = db[MONGO_COLLECTION_NAME]
    projects_cursor = collections.find()

    projects = []
    async for project in projects_cursor:
        projects.append(serialize_project(project))  # ObjectId 처리
    
    return {"projects": projects}

# @router.get("/projects", response_model=list[ProjectList])
# async def get_projects():

#     return fake_db

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