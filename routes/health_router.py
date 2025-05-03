from fastapi import APIRouter
from service.database import db_client

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/")
async def health_check():
    try:
        if db_client:
            print("👉 db_client 초기화 확인됨!")
            await db_client.admin.command("ping")
            return {"status": "ok", "message": "MongoDB is connected"}
        else:
            print("❌ db_client가 초기화되지 않았습니다!")
            return {"status": "error", "message": "MongoDB client not initialized"}
    except Exception as e:
        print(f"❌ Ping 실패: {e}")
        return {"status": "error", "message": f"Ping failed: {e}"}

