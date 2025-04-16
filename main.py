from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# .env 환경변수 불러오기
load_dotenv()

# FastAPI 앱 생성
app = FastAPI()

# CORS 설정 (React 개발 서버와 통신 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React 개발 서버 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB 연결
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["portfolio"]
project_col = db["projects"]

# 기본 라우터
@app.get("/")
def root():
    return {"message": "FastAPI is running"}

# 프로젝트 목록 API
@app.get("/detail/:id")
def get_projects():
    projects = list(project_col.find({}, {"title": 1, "description": 1}))
    for p in projects:
        p["_id"] = str(p["_id"])
    return projects
