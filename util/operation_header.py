import json
from util.operation_json import OperationJson
from base.runmethon import runmethon
class OperationHeader:

    def __init__(self, response):
        self.response = response

    def get_response_token(self):
        '''
        获取登录返回的token
        '''
        #print(self.response)
        #token=self.response["result"]["token"]
        #jsession2=self.response['JSESSIONID']
        #token = {"data":{"token":self.response['data']['token']}}
        #token={'content-type': 'application/json;charset=utf-8','Accept': 'application/json;charset=utf-8', 'Cookie': 'JSESSIONID=%s' % self.response}
        try:
            token1 = self.response
            print("get_response_token",token1)
            token = {'content-type': 'application/json;charset=utf-8', 'Accept': 'application/json;charset=utf-8',
                 'X-Access-Token': token1}

            def write_data(self, data):
                with open("./dataconfig/token.json", 'w') as fp:
                    fp.write(json.dumps(token))
            return token

        except:
            token = {'content-type': 'application/json;charset=utf-8', 'Accept': 'application/json;charset=utf-8'}
            return token



    def write_token(self):
        op_json = OperationJson()
        op_json.write_data(self.get_response_token())



if __name__ == '__main__':

    url = "http://xxxxx"

    data = {
        "username": "1111",
        "password": "123456"
    }
    run_method=runmethon()
    # res = json.dumps(requests.post(url, data).json())
    res=run_method.run_main('Post', url, data)
    op = OperationHeader(res)
    op.write_token()