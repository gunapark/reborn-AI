import redis
from fastapi import HTTPException
from app.exceptions.redis_exception import RedisAlreadyProcessedException, RedisFailedToAddPostIdException

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

PROCESSED_SET = "bemypet_post_ids"

def is_already_processed(post_id: str) -> bool:
    check =  r.sismember(PROCESSED_SET, post_id)
    if check == 1:
        raise RedisAlreadyProcessedException(post_id)
    return True

def add_processed_post_id(post_id: str) -> None:
    added = r.sadd(PROCESSED_SET, post_id)
    if added != 1:
        raise RedisFailedToAddPostIdException(post_id)


