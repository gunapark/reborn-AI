from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test_route():
  return {"message": "API테스트 엔드포인트입니다."}