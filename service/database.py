from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/?authSource=admin"

async def get_mongo_client():
    try:
        # MongoDB URI에 인증 정보 추가
        client = AsyncIOMotorClient(MONGO_URI)
        
        # 인증을 거친 후 ping 명령 실행
        await client.admin.command('ping')  # MongoDB가 연결되었는지 확인하는 ping 명령
        return client
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MongoDB 연결 실패: {str(e)}")


client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB_NAME]
