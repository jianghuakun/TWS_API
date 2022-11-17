import requests
import json
class runmethon_new:
    def post_main(self,url,data=None,header=None):
        r = None
        if header != None:
            r = requests.post(url=url, data=json.dumps(data), headers=header)

            #print(res.status_code)
            #print(res.json())
        else:
            r = requests.post(url=url, data=json.dumps(data))
        # 3、获取结果相应内容
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        # 4、内容存到字典
        res = dict()
        res["code"] = code
        res["body"] = body
        #print("post_main",res.json())

        # 5、字典返回
        return res



    def get_main(self,url,data=None,header=None):
        r = None
        if header != None:
            r = requests.get(url=url, data=data, headers=header, verify=False)

        else:
            r = requests.get(url=url, data=data, verify=False)
        # 3、获取结果相应内容
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        # 4、内容存到字典
        res = dict()
        res["code"] = code
        res["body"] = body
        # print("post_main",res.json())

        # 5、字典返回
        return res

    def run_main(self,method,url,data=None,header=None):
        r = None

        if method == 'POST':
            r = self.post_main(url, data, header)
            #res=json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
            #return res
        else:
            r = self.get_main(url, data, header)
            #return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        # 5、字典返回
        return r

