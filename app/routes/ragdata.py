from fastapi import APIRouter
from app.service.rag.ragdata_bemypet import getdata
from app.service.rag.chucnking import chunk_text_by_sentence
import os
import numpy as np

router = APIRouter()

@router.get("/pageUrl/{url}")
async def rag_data_route(url: str):
  text = getdata(url)
  chunks = chunk_text_by_sentence(text)
  #임베딩 + 원본 텍스트 따로 저장
  #임베딩 모델: upskyy/bge-m3-korean
  #원본 텍스트: Elastic search를 사용.
  return {"message": "!!"}

import torch
print(torch.backends.cudnn.enabled)
print(torch.backends.cudnn.version())

