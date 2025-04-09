from fastapi import APIRouter
from app.service.rag.ragdata_bemypet import getdata
from app.service.rag.chucnking import chunk_text_by_sentence
from app.service.rag.embedding import embedding_sentences
from app.redis_utils import redis_processed

router = APIRouter()

@router.get("/pageUrl/{url}")
async def rag_data_route(url: str):
    text = getdata(url)
    chunks = chunk_text_by_sentence(text)
    embedding_sentences(chunks, "bemypet")
    redis_processed(url)
    return {"message": "success"}


