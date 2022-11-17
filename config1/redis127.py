#redis获取验证码
#!/usr/bin/python3
from redis import StrictRedis
class redis127:
    redis1 = StrictRedis(host='192.168.100.127', port=6379, db=1,password="redis123456",decode_responses=True)
    #redis0=StrictRedis(host='192.168.100.127',port=6379,db=0,decode_responses=True)
    #decode_responses=True解决读出来数据为字节问题，就是都带b
    '''{b'zhangsan': b'1', b'lisi': b'2', b'wangwu': b'3', b'weide': b'4', b'haden': b'13', b'paul': b'3', b'geden': b'10', b'kapeila': b
'10'}
'''
s1=redis127.redis1
captchas=s1.keys("*")
for captcha1 in captchas:
    if ":" not in captcha1 and len(captcha1)==32:
        captcha=s1.get(captcha1)
        print(captcha)
    else:
        pass



