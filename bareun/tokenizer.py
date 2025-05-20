import sys
import google.protobuf.text_format as tf
import os
from dotenv import load_dotenv
from bareunpy import Tokenizer

# 프로젝트 루트에 있는 .env 파일 로드
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
# 환경변수에서 API 키 가져오기
BAREUN_API_KEY = os.getenv('BAREUN_API_KEY')


# If you have your own localhost bareun.
tokenizer = Tokenizer(BAREUN_API_KEY, 'localhost', 5757)
# or if you have your own bareun which is running on 10.8.3.211:15656.
# my_tokenizer = Tagger(BAREUN_API_KEY, '10.8.3.211', 15656)


# print results. 
tokenized = tokenizer.tokenize_list(["안녕하세요."])

# get protobuf message.
m = tokenized.msg()
tf.PrintMessage(m, out=sys.stdout, as_utf8=True)
print(tf.MessageToString(m, as_utf8=True))
print(f'length of sentences is {len(m.sentences)}')
## output : 2
print(f'length of tokens in sentences[0] is {len(m.sentences[0].tokens)}')
print(f'length of segments of first token in sentences[0] is {len(m.sentences[0].tokens[0].segments)}')
print(f'tagged of first token in sentences[0] is {m.sentences[0].tokens[0].tagged}')
print(f'first segment of first token in sentences[0] is {m.sentences[0].tokens[0].segments[0]}')
print(f'hint of first morph of first token in sentences[0] is {m.sentences[0].tokens[0].segments[0].hint}')

## Advanced usage.
for sent in m.sentences:
    for token in sent.tokens:
        for m in token.segments:
            print(f'{m.text.content}/{m.hint}')

# get json object
jo = tokenized.as_json()
print(jo)

# get tuple of segments
ss = tokenized.segments()
print(ss)
ns = tokenized.nouns()
print(ns)
vs = tokenized.verbs()
print(vs)
# postpositions: 조사
ps = tokenized.postpositions()
print(ps)
# Adverbs, 부사
ass = tokenized.adverbs()
print(ass)
ss = tokenized.symbols()
print(ss)
