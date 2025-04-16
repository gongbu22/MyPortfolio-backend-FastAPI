from fastapi import FastAPI
from routes.project import router as project_router

app = FastAPI()

# 라우터를 FastAPI 애플리케이션에 등록
app.include_router(project_router)

