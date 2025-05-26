from bareunpy import Corrector
import os
from dotenv import load_dotenv

# .env에서 API 키 로드
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
BAREUN_API_KEY = os.getenv('BAREUN_API_KEY')

# Corrector 인스턴스 초기화
corrector = Corrector(BAREUN_API_KEY, 'localhost', 5757)

# -----------------------------
# 1. 단일 문장 교정
# -----------------------------
single_text = "영수 도 줄기가 얇아서 시들을 것 같은 꽃에물을 주었다."
response = corrector.correct_error(single_text)

print("\n=== 단일 문장 맞춤법 검사 결과 ===")
print(f"원문: {response.origin}")
print(f"교정문: {response.revised}")

# -----------------------------
# 2. 복수 문장 교정
# -----------------------------
multi_texts = [
    "어머니 께서 만들어주신김치찌게가너무맵다며동생이울어버렸다.",
    "영수 도 줄기가 얇아서 시들을 것 같은 꽃에물을 주었다."
]

responses = corrector.correct_error_list(multi_texts)

print("\n=== 여러 문장 맞춤법 검사 결과 ===")
for i, sentence in enumerate(responses):
    print(f"[{i+1}] 원문: {sentence.origin}")
    print(f"    교정문: {sentence.revised}")

# -----------------------------
# 3. JSON 출력 (선택)
# -----------------------------
print("\n=== JSON 출력 ===")
for res in responses:
    corrector.print_as_json(res)
