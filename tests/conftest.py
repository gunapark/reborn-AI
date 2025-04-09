import pytest
import os
import sys

# 프로젝트 루트 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def sample_text():
    return "안녕하세요. 반갑습니다. 오늘은 좋은 날씨입니다." 