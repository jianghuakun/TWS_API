例子：
检查点示例：{"code":200,"key1_length":5,"key2_include":"abc","key3_type":"abd","key4_type":123,"key5_list":[1,2,3,5],"key6_range":range(1,10),"result":{"token_type":"abc","multiDepart_type":123,"key1_length":5,"key2_include":"abc"}}
对应测试用例：{
    "code": 1001,
    "message": "成功",
    "success": True,"key1":"abcde","key2":"ffabcdr","key3":"123","key4":1234,"key5":4,"key6":10,
                            "key13": [{"key7": {"key8": 123, "key9_length": "abcd", "key10": "ffeabcg",
                                                "key11": 4, "key12_range": 50}}],"result": {
        "key7":{"key8":123,"key9_length":4,"key10_include":"abc","key11_list":6,"key12_range":50},"key13":[{"key7":{"key8":123,"key9_length":4,"key10_include":"abc","key11_list":4,"key12_range":20}}],
                                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTUzMDQwNjQsInVzZXJuYW1lIjoiaXRyaW90YSJ9.1uFTbHfKfZ0jK-MtraER-kxSoKAYNhl6W2bnCS3FCh4",
        "multiDepart": 0,"key1":"qwert","key2":"aaabcde","key5":4,"key6":10,
        "userInfo": {
            "id": "1894794e5c594e6081325e296d97975f",
            "username": "itriota",
            "realname": "Bond Yin",
            "email": "bond.yinbangfei@fenda.com",
            "phone": "13728882956",
            "status": 1,
            "delFlag": 0,
            "workNo": "040394"
        }
    },
    "timestamp": 1595300464115
}
1.code值为200时，通用校验值为"code": 200,"message": "成功","success": True，程序已经嵌套
2.长度判断为：key_length,如："key1_length":5，表示响应数据key1长度为5，只有字符串才有长度
3.包含判断为：key_include，如："key2_include":"abc"，表示响应数据key2包含字符abc，只有字符串才有包含
4.类型判断为：key4_type,如："key3_type":"abd"，表示响应数据key3类型为字符串，适用于python数字、字符串、列表、集合、元组、字典类型
5.值在列表内判断为：key5_list，如："key5_list":[1,2,3,5],表示响应数据key5值必须在列表内
6.值在区间内判断：key6_range，如："key6_range":range(1,10)，表示响应数据key6值必须在区间（1,10)内，包含1，不含10
7.依赖说明：case说明：情况1：依赖case1(获取验证码），测试项无验证码超过1分钟；情况2：依赖case1(获取验证码），验证码超过1分钟；
                   依赖返回值：data-list-0-id即为data.list[0].id
                   请求数据依赖字段：gameTeamPlayerArgs-0-isStartingLineup，即为gameTeamPlayerArgs[0].isStartingLineup

