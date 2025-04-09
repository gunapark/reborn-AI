import redis
from fastapi import HTTPException
from app.exceptions.redis_exception import RedisAlreadyProcessedException, RedisFailedToAddPostIdException

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

PROCESSED_SET = "bemypet_post_ids"

def redis_processed(post_id: str):
    check =  r.sismember(PROCESSED_SET, post_id)
    if check == 1:
        print(f"post_id: {post_id} 이미 처리됨")
        raise RedisAlreadyProcessedException(post_id)
    else:
        add_processed_post_id(post_id)
        print(f"post_id: {post_id} 처리 완료")


def add_processed_post_id(post_id: str) -> None:
    added = r.sadd(PROCESSED_SET, post_id)
    if added != 1:
        raise RedisFailedToAddPostIdException(post_id)