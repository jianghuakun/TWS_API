import pymysql
from config1.mysql127 import db127
from config1.redis127 import redis127
#本方法为删除测试数据
class data_delete_ota:
    def user_delete(self):
        #删除账户1
        #print("删除账户1")
        #db127.itri_ota_cursor.execute("SELECT * FROM sys_user WHERE username='jiangtest3-选参少departIds0804'")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="13691249154"')
        #print("删除账户2")
        result = db127.itri_ota_cursor.fetchall()
        if len(result) == 0:
            pass
            #print("系统账户 不存在")
        else:
            #print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from sys_user where username='13691249154'")
            db127.itri_ota.commit()
            #print("删除系统账户成功")

        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="13234567821"')
        result1 = db127.itri_ota_cursor.fetchall()
        if len(result1) == 0:
            pass
            #print("系统账户 不存在")
        else:
            #print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from sys_user where username='13234567821'")
            db127.itri_ota.commit()
            #print("删除系统账户成功")

        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="jiangtest3-选参少departIds08043"')
        result2= db127.itri_ota_cursor.fetchall()
        if len(result2) == 0:
            pass
            #print("系统账户 不存在")
        else:
            #print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from sys_user where username='jiangtest3-选参少departIds08043'")
            db127.itri_ota.commit()
            #print("删除系统账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="jiangtest3-选参少departIds08044"')
        result3 = db127.itri_ota_cursor.fetchall()
        if len(result3) == 0:
            pass
            #print("系统账户 不存在")
        else:
            #print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from sys_user where username='jiangtest3-选参少departIds08044'")
            db127.itri_ota.commit()
            #print("删除系统账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="jiangtest3-选参少departIds08045"')
        result4 = db127.itri_ota_cursor.fetchall()
        if len(result4) == 0:
            pass
            #print("系统账户 不存在")
        else:
            #print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from sys_user where username='jiangtest3-选参少departIds08045'")
            db127.itri_ota.commit()
            #print("删除系统账户成功")

        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="jiangtest3-depart选参少workNo"')
        result41 = db127.itri_ota_cursor.fetchall()
        if len(result41) == 0:
            pass
            # print("系统账户 不存在")
        else:
            # print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from sys_user where username='jiangtest3-depart选参少workNo'")
            db127.itri_ota.commit()
            # print("删除系统账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="jiangtestsetpwd1123"')
        result42 = db127.itri_ota_cursor.fetchall()
        if len(result42) == 0:
            pass
            # print("系统账户 不存在")
        else:
            # print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from sys_user where username='jiangtestsetpwd1123'")
            db127.itri_ota.commit()
            # print("删除系统账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="jiangtestsetpwd113211210804001"')
        result43 = db127.itri_ota_cursor.fetchall()
        if len(result43) == 0:
            pass
            # print("系统账户 不存在")
        else:
            # print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from sys_user where username='jiangtestsetpwd113211210804001'")
            db127.itri_ota.commit()
            # print("删除系统账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="jiangtest3-选参少departIds08043"')
        result44 = db127.itri_ota_cursor.fetchall()
        if len(result44) == 0:
            pass
            # print("系统账户 不存在")
        else:
            # print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from sys_user where username='jiangtest3-选参少departIds08043'")
            db127.itri_ota.commit()
            # print("删除系统账户成功")
        #构造部门用户
        #构造部门用户-关联1个部门

        #print(123,len(result))
        # 构造部门用户-关联2个部门
        # 构造部门用户-关联3个部门
        #构造系统用户


        return result
    #删除测试增加的1级部门
    def depart_delete(self):

        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增1级部门少1"')
        result1 = db127.itri_ota_cursor.fetchall()

        if len(result1) == 0:
            pass
            #print("系统账户 不存在")
        else:
            #print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增1级部门少1'")
            db127.itri_ota.commit()
            #print("删除系统账户成功")

        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增1级部门少2"')
        result2 =db127.itri_ota_cursor.fetchall()

        if len(result2)==0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增1级部门少2'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增1级部门少3"')
        result3 = db127.itri_ota_cursor.fetchall()

        if len(result3) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增1级部门少3'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增1级部门少5"')
        result4 = db127.itri_ota_cursor.fetchall()

        if len(result4) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增1级部门少5'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增1级部门少6"')
        result5 = db127.itri_ota_cursor.fetchall()

        if len(result5) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增1级部门少6'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增1级部门少7"')
        result6 = db127.itri_ota_cursor.fetchall()
        if len(result6) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增1级部门少7'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")

        # 删除测试新增6个2级部门
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增1级部门少8"')
        result7 = db127.itri_ota_cursor.fetchall()

        if len(result7) == 0:
            pass
            #print("系统账户 不存在")
        else:
            #print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增1级部门少8'")
            db127.itri_ota.commit()
            #print("删除系统账户成功")

        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增1级部门少9"')
        result8 = db127.itri_ota_cursor.fetchall()

        if len(result8) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增1级部门少9'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增1级部门少10"')
        result9 = db127.itri_ota_cursor.fetchall()

        if len(result9) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增1级部门少10'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增2级部门少11"')
        result10 = db127.itri_ota_cursor.fetchall()

        if len(result10) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增2级部门少11'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增2级部门少12"')
        result11 = db127.itri_ota_cursor.fetchall()

        if len(result11) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增2级部门少12'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增2级部门少13"')
        result12 = db127.itri_ota_cursor.fetchall()

        if len(result12) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增2级部门少13'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")

        #删除3级部门新增6个部门
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增2级部门少14"')
        result13 = db127.itri_ota_cursor.fetchall()

        if len(result13) == 0:
            pass
            #print("系统账户 不存在")
        else:
            #print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增2级部门少14'")
            db127.itri_ota.commit()
            #print("删除系统账户成功")

        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增2级部门少15"')
        result14 = db127.itri_ota_cursor.fetchall()

        if len(result14) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增2级部门少15'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增2级部门少16"')
        result15 = db127.itri_ota_cursor.fetchall()

        if len(result15) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增2级部门少16'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增3级部门少17"')
        result16 = db127.itri_ota_cursor.fetchall()

        if len(result16) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增3级部门少17'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增3级部门少18"')
        result17 = db127.itri_ota_cursor.fetchall()

        if len(result17) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增3级部门少18'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增3级部门少19"')
        result18 = db127.itri_ota_cursor.fetchall()

        if len(result18) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增3级部门少19'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")

        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增3级部门少20"')
        result19 = db127.itri_ota_cursor.fetchall()

        if len(result19) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增3级部门少20'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")

        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增3级部门少21"')
        result20 = db127.itri_ota_cursor.fetchall()

        if len(result20) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增3级部门少21'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")

        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="新增3级部门少22"')
        result21 = db127.itri_ota_cursor.fetchall()

        if len(result21) == 0:
            print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute("delete from sys_depart where depart_name='新增3级部门少22'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")

        db127.itri_ota_cursor.execute(
            'SELECT * FROM sys_depart WHERE depart_name="新增1级部门少4"')
        result22 = db127.itri_ota_cursor.fetchall()

        if len(result22) == 0:
            pass
            #print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute(
                "delete from sys_depart where depart_name='新增1级部门少4'")
            db127.itri_ota.commit()
            #print("删除关联一个部门账户成功")
        #删除部门账户测试跨部门账户
        db127.itri_ota_cursor.execute(
            'SELECT * FROM sys_depart WHERE depart_name="3级部门1"')
        result23 = db127.itri_ota_cursor.fetchall()

        if len(result23) == 0:
            pass
            # print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute(
                "delete from sys_depart where depart_name='3级部门1'")
            db127.itri_ota.commit()
            # print("删除关联一个部门账户成功")
        db127.itri_ota_cursor.execute(
            'SELECT * FROM sys_depart WHERE depart_name="3级部门161"')
        result23 = db127.itri_ota_cursor.fetchall()

        if len(result23) == 0:
            pass
            # print("关联一个部门账户 不存在")
        else:
            db127.itri_ota_cursor.execute(
                "delete from sys_depart where depart_name='3级部门161'")
            db127.itri_ota.commit()
            # print("删除关联一个部门账户成功")



        #print(123,len(result))
        # 构造部门用户-关联2个部门
        # 构造部门用户-关联3个部门
        #构造系统用户


        return None
    #删除新增版本
    def version_delete(self):

        db127.itri_ota_cursor.execute('SELECT * FROM t_version WHERE task_name="ota1.0版本测试"')
        result11 = db127.itri_ota_cursor.fetchall()

        if len(result11) == 0:
            pass
        else:
            # print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from t_version WHERE task_name='ota1.0版本测试'")
            db127.itri_ota.commit()
            # print("删除系统账户成功")

        db127.itri_ota_cursor.execute('SELECT * FROM t_version WHERE file_id="3b94aedd2dc44a2ebb13bdfc83d20338"')
        result1 = db127.itri_ota_cursor.fetchall()

        if len(result1) == 0:
            pass
        else:
            #print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from t_version WHERE file_id='3b94aedd2dc44a2ebb13bdfc83d20338'")
            db127.itri_ota.commit()
            #print("删除系统账户成功")

    def user_group_delete(self):

        db127.itri_ota_cursor.execute('SELECT * FROM t_user_group WHERE group_name="userwhileauto1"')
        result11 = db127.itri_ota_cursor.fetchall()

        if len(result11) == 0:
            pass
        else:
            # print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from t_user_group WHERE group_name='userwhileauto1'")
            db127.itri_ota.commit()
            # print("删除系统账户成功")

        db127.itri_ota_cursor.execute('SELECT * FROM t_user_group WHERE group_name="userwhileauto2"')
        result1 = db127.itri_ota_cursor.fetchall()

        if len(result1) == 0:
            pass
        else:
            # print("删除系统账户成功")
            db127.itri_ota_cursor.execute("delete from t_user_group WHERE group_name='userwhileauto2'")
            db127.itri_ota.commit()
            # print("删除系统账户成功")
    #删除新增的出厂版本
    def version_factory_delete(self):

        db127.itri_ota_cursor.execute(
            'SELECT * FROM t_version_factory WHERE depart_id="10611880139241048990bd5d7f4be58c" and version="1.0.5"')
        result = db127.itri_ota_cursor.fetchall()
        print(result)

        if len(result) == 0:
            pass
        else:
            db127.itri_ota_cursor.execute("DELETE FROM t_version_factory WHERE depart_id='10611880139241048990bd5d7f4be58c' and version='1.0.5'")
            db127.itri_ota.commit()

