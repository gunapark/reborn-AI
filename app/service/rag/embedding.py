from sentence_transformers import SentenceTransformer
import numpy as np
import torch
import logging
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="upskyy/bge-m3-korean",
    model_kwargs={"device": "cuda"},
    encode_kwargs={"batch_size": 64, "show_progress_bar": True}
)

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# GPU 사용 가능 여부 확인
device = "cuda" if torch.cuda.is_available() else "cpu"
logger.info(f"Using device: {device}")
if device == "cuda":
    logger.info(f"GPU: {torch.cuda.get_device_name(0)}")
    logger.info(f"GPU 메모리: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f}GB")

# 모델 로드
logger.info("모델 로딩 중...")
model = SentenceTransformer('upskyy/bge-m3-korean')
model.to(device)
logger.info("모델 로딩 완료")


def embedding_sentences(sentence_list, source="bemypet"):
    logger.info(f"임베딩 시작: {len(sentence_list)}개 문장")
    # 임베딩 생성
    embeddings = model.encode(sentence_list, convert_to_numpy=True)
    
    # 메타데이터와 함께 결과 반환
    results = []
    for sentence, embedding in zip(sentence_list, embeddings):
        results.append({
            "text": sentence,
            "embedding": embedding,
            "metadata": {"source": source}
        })
    
    logger.info("임베딩 완료")
    return results


# 테스트 코드
if __name__ == "__main__":
    # 테스트 문장들
    test_sentences = [
        "강아지가 혀를 날름거리는 이유는 무엇인가요?",
        "고양이는 왜 박스를 좋아할까?",
        "햄스터는 왜 뺨에 먹이를 넣을까?"
    ]
    
    # 임베딩 테스트
    results = embedding_sentences(test_sentences, "test")
    
    # 결과 확인
    for result in results:
        print(f"\n문장: {result['text']}")
        print(f"임베딩 벡터 크기: {result['embedding'].shape}")
        print(f"출처: {result['metadata']['source']}")


