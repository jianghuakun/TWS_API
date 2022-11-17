from util.operation_excel import OperationExcel
from base.runmethon import runmethon
from data.get_data import GetData
import json
from util.operation_header import OperationHeader
import requests
from util.operation_json import OperationJson
from base.md51 import sing_md5
import base.md5_32
from config.redis127 import redis127
import time
class DependentData:
    """解决数据依赖问题"""

    def __init__(self, case_id):
        self.case_id = case_id
        #print(case_id, self.case_id)
        self.opera_excel = OperationExcel()
        self.data = GetData()
        self.run_method = runmethon()
        self.md51 = sing_md5()

    def get_case_line_data(self):
        """
        通过case_id去获取该case_id的整行数据
        :param case_id: 用例ID
        :return:
        """

        rows_data = self.opera_excel.get_row_data(self.case_id)

        return rows_data

    def run_dependent(self):
        """
        执行依赖测试，获取结果
        :return:
        """
        run_method = runmethon()
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_request_data(row_num)
        # header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        header = self.data.is_header(row_num)
        #调用md5加密替换成新的url
        params = self.data.get_params(row_num)
        name=self.data.get_request_name(row_num)


        sign = self.md51.newsign(row_num)
        url += sign
        urls = []
        #print(params)
        if params != None:
            param = ''
            for key in params.keys():
                param1 = [param, key, "=", params[key], "&"]
                param = "".join(param1)
            param = param[:-1]
            url = url + "&" + param
            urls.append(url)
        #print(request_data,url,header,method,row_num)
        #token签名方式
        if header == "write":
            herders = {'content-type': 'application/json;charset=utf-8',
                       'Accept': 'application/json;charset=utf-8'
                       }
            try:
                res = self.run_method.run_main(method, url, request_data, herders)
                # print(urls[0], url,type(json.loads(res)))
                if "result" in res:
                    #print(123456, type(res), res, 321)
                    token = dict(res)["result"]["token"]
                    #print("run", token)
                    op_header = OperationHeader(token)
                    op_header.write_token()
                else:
                    print("no token")
                    print(dict(res)["code"])

                # token = dict(r.json())["result"]["token"]

            except:
                res = str({"error code": 404})

            if method == "POST":
                try:
                    r = requests.post(url, data=json.dumps(request_data), headers=herders)
                    # JSESSIONID在headers中
                    # JSESSIONID = dict(r.cookies)['JSESSIONID']
                    # token在body中
                    # print("post",r.json())
                    token = dict(r.json())["result"]["token"]
                    op_header = OperationHeader(token)
                    op_header.write_token()
                except:
                    pass
                    # res = str({"error code":404})


            else:
                try:
                    r = requests.get(url, request_data)
                    token = dict(r.json())["result"]["token"]
                    op_header = OperationHeader(token)
                    # op_header = OperationHeader(dict(r.cookies))
                    op_header.write_token()
                except:
                    pass
                    # res = str({"error code":404})




        elif header == 'yes':
            op_json = OperationJson("./dataconfig/token.json")
            jsession2 = op_json.get_data('X-Access-Token')
            # request_data = dict(request_data, **token)  # 把请求数据与登录token合并，并作为请求数据
            herders = {'content-type': 'application/json;charset=utf-8',
                       'Accept': 'application/json;charset=utf-8', 'X-Access-Token': jsession2}
            # print(urls[0], url,herders)
            try:
                res = self.run_method.run_main(method, url, request_data, herders)
            except:
                res = str({"error code": 404})
        else:
            try:
                res = self.run_method.run_main(method, url, request_data)
            except:
                res = str({"error code": 404})
        '''
               #JSESSIONID签名方式
                       if header == "write":
                   herders = {'content-type': 'application/json;charset=utf-8',
                              'Accept': 'application/json;charset=utf-8'
                              }
                   res = self.run_method.run_main(method, url, request_data, herders)
                   op_header = OperationHeader(res)
                   op_header.write_token()
                   if method == "POST":
                       r = requests.post(url, data=json.dumps(request_data), headers=herders)

                       JSESSIONID = dict(r.cookies)['JSESSIONID']
                       op_header = OperationHeader(JSESSIONID)
                       op_header.write_token()
                   else:
                       res = requests.get(url, request_data)
                       op_header = OperationHeader(dict(res.cookies))
                       op_header.write_token()


               elif header == 'yes':
                   op_json = OperationJson("./dataconfig/token.json")
                   jsession2 = op_json.get_data('Cookie')
                   # request_data = dict(request_data, **token)  # 把请求数据与登录token合并，并作为请求数据
                   herders = {'content-type': 'application/json;charset=utf-8',
                              'Accept': 'application/json;charset=utf-8', 'Cookie': 'JSESSIONID=%s' % jsession2}
                   res = self.run_method.run_main(method, url, request_data, herders)
               else:
                   res = self.run_method.run_main(method, url, request_data)
               #print(json.loads(res))
               return json.loads(res)
               '''
        return res



    def get_data_for_key(self, row):
        """
        根据依赖的key去获取执行依赖case的响应然后返回
        :return:
        """
        pass
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        #依赖返回值,先判断是列表还是key,如果是列表表示依赖结果有多层json再根据key逐个获取
        depend_data_1=depend_data.split("-")
        key1=response_data
        if type(key1)==type("abd"):
            #print("abd".replace("a","A"),key1)
            key1.replace("false","False").replace("true","True")
            key1=json.loads(key1)
        else:
            pass
        if len(depend_data_1)==1:
            key1=key1.get(depend_data_1[0])
        else:
            for i in depend_data_1:
                try:
                    one_num=int(i)
                    key1 = key1[one_num]
                except:
                    key1 = key1.get(i)
        #print(key1)



        #print(123,response_data,depend_data)
        #return [match.value for match in parse(depend_data).find(response_data)][0]
        #print([match.value for match in parse(depend_data).find(response_data)][0])
        #return response_data.get("data").get("list")[0].get("id")

        #print(113344, self.data.get_request_name(row))
        if self.case_id=="case_01" and "验证码超过1分钟" not in self.data.get_request_name(row):
            s1 = redis127.redis1
            captchas = s1.keys("*")
            for captcha1 in captchas:

                if ":" not in captcha1 and len(captcha1) == 32:
                    key1 = s1.get(captcha1)[1:-1]
                    #print(123,key1,len(key1))

                else:

                    pass

        #验证码超过1分钟,sleep 1 分钟
        elif "验证码超过1分钟" in self.data.get_request_name(row):
            s1 = redis127.redis1
            captchas = s1.keys("*")
            for captcha1 in captchas:

                if ":" not in captcha1 and len(captcha1) == 32:
                    key1 = s1.get(captcha1)[1:-1]
                    #print(123, key1, len(key1))

                else:

                    pass
            #print(134)
            time.sleep(120)
        else:
            pass
        #print(123, key1)
        return key1

if __name__ == '__main__':
    opera = OperationExcel()
    opera.get_data()
    print(opera.get_data().nrows)
    print(opera.get_lines())
    print(opera.get_cell_value(1, 2))