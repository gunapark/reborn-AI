import pytest
from app.service.rag.chucnking import chunk_text_by_sentence

def test_chunk_text_by_sentence_basic():
    # 기본적인 테스트 케이스
    text = "안녕하세요. 반갑습니다. 오늘은 좋은 날씨입니다."
    chunks = chunk_text_by_sentence(text, max_chunk_size=20)
    assert len(chunks) > 1
    assert all(len(chunk) <= 20 for chunk in chunks)

def test_chunk_text_by_sentence_empty():
    # 빈 텍스트 테스트
    text = ""
    chunks = chunk_text_by_sentence(text)
    assert len(chunks) == 0

def test_chunk_text_by_sentence_single():
    # 단일 문장 테스트
    text = "안녕하세요."
    chunks = chunk_text_by_sentence(text)
    assert len(chunks) == 1
    assert chunks[0] == "안녕하세요."

def test_chunk_text_by_sentence_large():
    # 큰 텍스트 테스트
    text = "안녕하세요. " * 100
    chunks = chunk_text_by_sentence(text, max_chunk_size=100)
    assert len(chunks) > 1
    assert all(len(chunk) <= 100 for chunk in chunks) 