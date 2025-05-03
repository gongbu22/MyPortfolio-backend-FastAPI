from fastapi import FastAPI
from contextlib import asynccontextmanager
from service.database import init_db
from fastapi.middleware.cors import CORSMiddleware
from routes.project import router as project_router
from routes.health_router import router as health_router
from dotenv import load_dotenv
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()  # 앱 시작 시 DB 초기화
    yield
    # 앱 종료 시 종료 작업이 있다면 여기에 추가

app = FastAPI(lifespan=lifespan)

react_host = os.getenv("REACT_APP_HOST", "http://localhost").rstrip("/")
react_port = os.getenv("REACT_APP_PORT", "5173")

origins = [
    f"${react_host}:${react_port}",
    "http://localhost:5173",
    "http://127.0.0.1:5173"  # React 프론트엔드 허용
]

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # React 앱이 동작하는 주소 (개발 중)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

app.include_router(project_router)
app.include_router(health_router)

