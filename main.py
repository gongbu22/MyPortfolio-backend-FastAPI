from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.project import router as project_router

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 앱이 동작하는 주소 (개발 중)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

app.include_router(project_router)

