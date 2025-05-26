import sys
import google.protobuf.text_format as tf
import os
from dotenv import load_dotenv
from bareunpy import Tagger

# 프로젝트 루트에 있는 .env 파일 로드
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
# 환경변수에서 API 키 가져오기
BAREUN_API_KEY = os.getenv('BAREUN_API_KEY')
SERVER_HOST=os.getenv('SERVER_HOST')
SERVER_PORT=os.getenv('SERVER_PORT')


# If you have your own localhost bareun.
tagger=Tagger(BAREUN_API_KEY, SERVER_HOST, SERVER_PORT)

# or if you have your own bareun which is running on 10.8.3.211:15656.
# my_tagger = Tagger(BAREUN_API_KEY, '10.8.3.211', 15656)


# print results. 
res = tagger.tags(["안녕하세요."])

# get protobuf message.
m = res.msg()
tf.PrintMessage(m, out=sys.stdout, as_utf8=True)
print(tf.MessageToString(m, as_utf8=True))
print(f'length of sentences is {len(m.sentences)}')
## output : 2
print(f'length of tokens in sentences[0] is {len(m.sentences[0].tokens)}')
print(f'length of morphemes of first token in sentences[0] is {len(m.sentences[0].tokens[0].morphemes)}')
print(f'lemma of first token in sentences[0] is {m.sentences[0].tokens[0].lemma}')
print(f'first morph of first token in sentences[0] is {m.sentences[0].tokens[0].morphemes[0]}')
print(f'tag of first morph of first token in sentences[0] is {m.sentences[0].tokens[0].morphemes[0].tag}')

## Advanced usage.
for sent in m.sentences:
    for token in sent.tokens:
        for m in token.morphemes:
            print(f'{m.text.content}/{m.tag}:{m.probability}:{m.out_of_vocab}')

# get json object
jo = res.as_json()
print(jo)

# get tuple of pos tagging.
pa = res.pos()
print(pa)
# another methods
ma = res.morphs()
print(ma)
na = res.nouns()
print(na)
va = res.verbs()
print(va)

# custom dictionary
cust_dic = tagger.custom_dict("my")
cust_dic.copy_np_set({'내고유명사', '우리집고유명사'})
cust_dic.copy_cp_set({'코로나19'})
#cust_dic.copy_cp_caret_set({'코로나^백신', '"독감^백신'})
cust_dic.update()

# laod prev custom dict
cust_dict2 = tagger.custom_dict("my")
cust_dict2.load()

tagger.set_domain('my')
tagger.pos('코로나19는 언제 끝날까요?')