import json
class CommonUtil:
    def is_contain(self, str_one, str_two):
        """
        判断一个字符串是否在另一个字符串中
        :param str_one:
        :param str_two:
        :return:
        """
        flag = None
        print(str_two)
        #str_two_tr=str_two.replace("null","1234").replace("true","True").replace("false","False")
        #str_two_dic=eval(str_two_tr)
        #str_one_tr=eval(str_one)

        """
                for key in str_one.keys():
            if str_one.get(key) == "test1234":
                if key in str_two:
                    flag = True
                else:
                    flag = False
                return flag
            else:
                if key in str_two_dic.keys():
                    if str_one.get(key)==str_two_dic.get(key):
                        flag = True
                    else:
                        flag = False
                else:
                    flag = False
                return flag
        """
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag



