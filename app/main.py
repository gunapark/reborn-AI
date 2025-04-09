from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from app.routes import test, ragdata

app = FastAPI(title="RE:BORN AI SERVER", description="RE:BORN AI SERVER", version="1.0.0")

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
  return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
  return JSONResponse(status_code=500, content={"message": str(exc)})

#라우터 추가
app.include_router(test.router, prefix="/api")
app.include_router(ragdata.router, prefix="/api")

@app.get("/")
async def root():
  return {"message": "RE:BORN AI SERVER입니다"}


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("app.main:app",host="0.0.0.0", port=8000, reload=True)