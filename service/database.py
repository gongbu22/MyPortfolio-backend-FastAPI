from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from fastapi import HTTPException
from dotenv import load_dotenv
import os
from models.projects import myportfolio

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/?authSource=admin"

db_client = None  # 전역 DB 클라이언트

async def init_db():
    global db_client
    try:
        print("👉 MongoDB 연결 시도 중...")
        db_client = AsyncIOMotorClient(MONGO_URI)
        database = db_client[MONGO_DB_NAME]
        # print("Database: ", database)
        await init_beanie(database=database, document_models=[myportfolio])
        print("✅ MongoDB 연결 및 Beanie 초기화 완료!")
    except Exception as e:
        print(f"❌ MongoDB 연결 실패: {e}")  # 여기에 진짜 에러 원인이 출력됨
        raise

