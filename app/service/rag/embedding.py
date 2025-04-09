from sentence_transformers import SentenceTransformer
import numpy as np
import torch
import logging
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings
import os
from fastapi import HTTPException

logger = logging.getLogger(__name__)

embedding_model = HuggingFaceEmbeddings(
    model_name="upskyy/bge-m3-korean",
    model_kwargs={"device": "cuda"},
    encode_kwargs={"batch_size": 64}
)


def embedding_sentences(sentence_list, source="bemypet", index_name='faiss_dog'):
    docs = [Document(page_content=sentence, metadata={"source": source}) for sentence in sentence_list]
    if(os.path.exists(index_name)):
        print(f"index_name: {index_name} 존재")
        vectorstore = FAISS.load_local(index_name, embedding_model, allow_dangerous_deserialization=True)
        vectorstore.add_documents(docs)
    else:
        print(f"index_name: {index_name} 존재하지 않음")
        vectorstore = FAISS.from_documents(docs, embedding_model)
    vectorstore.save_local(index_name)

  


