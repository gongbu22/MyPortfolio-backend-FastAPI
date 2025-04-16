# import motor.motor_asyncio
# from bson.objectid import ObjectId
# from typing import List
# from models.project import Project

# # MongoDB URI 설정
# MONGO_DETAILS = "mongodb://localhost:27017"  # 로컬에서 MongoDB가 실행되는 주소
# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
# database = client["myportfolio"]  # MongoDB의 데이터베이스 이름
# project_collection = database["projects"]  # 프로젝트 데이터가 저장될 컬렉션

# # 프로젝트 추가
# async def add_project(project: Project):
#     project_dict = project.dict()
#     result = await project_collection.insert_one(project_dict)
#     return str(result.inserted_id)

# # 모든 프로젝트 가져오기
# async def get_projects() -> List[Project]:
#     projects = []
#     cursor = project_collection.find()
#     async for document in cursor:
#         project = Project(**document)
#         projects.append(project)
#     return projects

# # 특정 프로젝트 ID로 프로젝트 가져오기
# async def get_project_by_id(project_id: str) -> Project:
#     document = await project_collection.find_one({"_id": ObjectId(project_id)})
#     if document:
#         return Project(**document)
#     return None
