from locust import HttpUser
from locust import task
import os
import json
#我们在做接口自动化测试时，使用的是request对接口发起请求，在这里我们用的是locust中的httpuser对接口进行发起请求
class opms(HttpUser):
    def on_start(self):
        print("我是一个用户，我启动了")
    def on_stop(self):
        print("我是一个用户，我退出了")
#定义好的接口必须使用task装饰器使其成为一个需要执行的任务，否则的话即使启动了locust也不会将定义好的函数作为一个需要执行的任务
    @task
    def login(self):
        url="/brand/sms/open/sendCaptcha"
        #with self.client.get(url=url,name="获取登录页",catch_response=True) as res:
            # 下面断言，当我们返回的text中有项目管理则登录成功，反之失败
            #if "项目管理" in res.text:
            #    res.success()
            #else:
                #res.failure("登录失败")
    @task
    def postlogin(self):
        url="/brand/sms/open/sendCaptcha"
        herders = {'content-type': 'application/json;charset=utf-8',
                   'Accept': 'application/json;charset=utf-8'}
        data={
	"msisdn": "13691699127"
}
        with self.client.post(url,data=json.dumps(data),headers=herders,name="登录",catch_response=True) as res:
            print(res.json())
            if res.json()["code"]==10022:
                res.success()
            else:
                res.failure("登录失败")
if __name__ == '__main__':
    os.system("locust -f loginLocust.py --web-host=127.0.0.1")