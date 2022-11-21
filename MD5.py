import hashlib
import time
print(str(time.time())[0:10])
import uuid

print(str(uuid.uuid4()).replace("-","")[:20])
def md5(str):
    obj = hashlib.md5()
    obj.update(str)
    return obj.hexdigest().upper()
str1="apikey=fendaitripjota2020&apisecret=93d31fc184436a5ce61ab74363260e26c48cd5c4&nonce=123123123123&timestamp=1593482301"
print(md5(str1.encode(encoding="utf-8")))
s1={}
s1["name"]="zhang"
print(s1)
