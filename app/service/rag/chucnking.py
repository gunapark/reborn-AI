import spacy

nlp = spacy.load("ko_core_news_md")

def chunk_text_by_sentence(text, max_chunk_size=512):
    """
    텍스트를 문장 단위로 분할합니다.
    
    Args:
        text: 분할할 텍스트
        max_chunk_size: 최대 청크 크기
    """
    doc = nlp(text)
    sentences = list(doc.sents)
    chunks = []
    current_chunk = []
    current_length = 0

    for i, sent in enumerate(sentences):
        sent_length = len(sent.text)
        
        if current_length + sent_length <= max_chunk_size:
            current_chunk.append(sent.text)
            current_length += sent_length
        else:
            if current_chunk:
                chunks.append(" ".join(current_chunk))
                # 마지막 1문장만 유지
                current_chunk = current_chunk[-1:]
                current_length = len(current_chunk[0])
            current_chunk.append(sent.text)
            current_length += sent_length

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

