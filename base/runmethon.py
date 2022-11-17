import requests
import json
#封装requests方法
class runmethon:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=json.dumps(data), headers=header)

            #print(res.status_code)
            #print(res.json())
        else:
            res = requests.post(url=url, data=json.dumps(data))
        #print("post_main",res.json())
        return res.json()



    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False)

        else:
            res = requests.get(url=url, data=data, verify=False)

        return res.json()

    def run_main(self,method,url,data=None,header=None):
        res = None

        if method == 'POST':
            res = self.post_main(url, data, header)
            #res=json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
            return res
        else:
            res = self.get_main(url, data, header)
            return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)


