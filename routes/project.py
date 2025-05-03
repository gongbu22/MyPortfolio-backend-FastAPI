from fastapi import APIRouter, HTTPException
from service.project_service import get_all_projects, get_detail
from typing import List, Dict
# from dotenv import load_dotenv
# import os

# 환경변수 로드
# load_dotenv()

# MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")

router = APIRouter()

@router.get("/projects", response_model=Dict[str, List[dict]])
async def get_all_projects_data():
    try:
        projects = await get_all_projects()
        return {
            "projects": [
                { 
                    "num": str(project.num),
                    "title": project.title,
                    "overview": project.overview,
                    "design": project.design,
                    "tech_stack": project.tech_stack,
                    "expected_outcomes": project.expected_outcomes,
                    "github": project.github,
                    "web": project.web,
                    "features": project.features
                }
                for project in projects
            ]
        }
    except Exception as e:
        print("🔥 MongoDB 에러:", e)
        raise HTTPException(status_code=500, detail="DB 연결 실패")

@router.get("/detail/{project_num}", response_model=dict)
async def get_project_detail(project_num: str):
    project = await get_detail(project_num)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return { 
                "num": str(project.num),
                "title": project.title,
                "overview": project.overview,
                "design": project.design,
                "tech_stack": project.tech_stack,
                "expected_outcomes": project.expected_outcomes,
                "github": project.github,
                "web": project.web,
                "features": project.features
            }


# def serialize_project(project) -> dict:
#     project["_id"] = str(project["_id"])
#     return project

# @router.get("/test_mongo")
# async def test_mongo_connection():
#     # MongoDB 연결 확인
#     client = await get_mongo_client()
    
#     # 연결된 MongoDB에서 DB 목록을 가져와서 확인
#     databases = await client.list_database_names()
    
#     return {"message": "MongoDB 연결 성공", "databases": databases}

# @router.get("/projects")
# async def root():
#     collections = db[MONGO_COLLECTION_NAME]
#     projects_cursor = collections.find()

#     projects = []
#     async for project in projects_cursor:
#         projects.append(serialize_project(project))  # ObjectId 처리
    
#     return {"projects": projects}

# # 특정 프로젝트 조회
# async def get_detail(project_id: str):
#     collections = db[MONGO_COLLECTION_NAME]

#     try:
#         detail = await collections.find_one({"id": int(project_id)})
#         if detail:
#             return serialize_project(detail)
#         return None
#     except Exception as e:
#         print("상세 데이터 에러")
#         return None    

# @router.get("/detail/{project_id}")
# async def fetch_project(project_id: str):
#     project = await get_detail(project_id)
#     if project is None:
#         raise HTTPException(status_code=404, detail="Project not found")
#     return project