import requests
from fastapi import HTTPException
from bs4 import BeautifulSoup
import re

headers = {"User-Agent": "Mozilla/5.0"}
advertisement_keywords = ["쿠팡 파트너스", "수수료", "협찬", "광고비"]

def getdata(url:str):
  response = requests.get(f"https://mypetlife.co.kr/{url}", headers=headers)
  soup = BeautifulSoup(response.text, "html.parser")
  page_content = soup.select_one(".entry-content.entry.clearfix")

  if page_content:
    # ✅ HTML 태그 없이 순수한 텍스트만 가져오기 (줄바꿈 포함)
    raw_text = page_content.get_text(separator="\n", strip=True)
    # ✅ 불필요한 줄바꿈 제거 (빈 줄 제거 + 여러 개의 줄바꿈을 하나로 정리)
    cleaned_text = "\n".join(line.strip() for line in raw_text.splitlines() if line.strip())
    text = re.sub(r"비마이펫 Q&A 커뮤니티[\s\S]*", "", cleaned_text)
    text = text.strip()
    
    # ✅ 광고 키워드 제거
    if any(keyword in text for keyword in advertisement_keywords):
      print(f"❌ 광고 키워드가 포함되어 있습니다.")
      raise HTTPException(status_code=400, detail="❌ 광고 키워드가 포함되어 있습니다.")
  
  else:
    raise HTTPException(status_code=400, detail="❌ 본문을 찾을 수 없습니다.")
  
  return text