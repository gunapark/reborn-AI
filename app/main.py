from fastapi import FastAPI
from app.routes import test

app = FastAPI()

#라우터 추가
app.include_router(test.router, prefix="/api")

@app.get("/")
async def root():
  return {"message": "RE:BORN AI SERVER입니다"}


if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app,host="0.0.0.0", port=8000, reload=True)