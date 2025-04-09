from fastapi import HTTPException

class RedisAlreadyProcessedException(HTTPException):
    def __init__(self, post_id: str):
        super().__init__(status_code=400, detail=f"Post_id: {post_id} is already processed")

class RedisFailedToAddPostIdException(HTTPException):
    def __init__(self, post_id: str):
        super().__init__(status_code=400, detail=f"Failed to add post_id: {post_id} to processed set")

