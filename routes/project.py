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

@router.get("/projects")
async def root():
    collections = db[MONGO_COLLECTION_NAME]
    projects_cursor = collections.find()

    projects = []
    async for project in projects_cursor:
        projects.append(serialize_project(project))  # ObjectId 처리
    
    return {"projects": projects}

# 특정 프로젝트 조회
async def get_detail(project_id: str):
    collections = db[MONGO_COLLECTION_NAME]

    try:
        detail = await collections.find_one({"id": int(project_id)})
        if detail:
            return serialize_project(detail)
        return None
    except Exception as e:
        print("상세 데이터 에러")
        return None    

@router.get("/detail/{project_id}")
async def fetch_project(project_id: str):
    project = await get_detail(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project