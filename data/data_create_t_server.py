import pymysql
from config1.mysql127 import db127
from config1.redis127 import redis127
#本方法为构造测试数据
class data_create_ota:
    def user_create(self):
        #构造系统账户
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="jiangtest091201"')
        result = db127.itri_ota_cursor.fetchall()
        sql = "insert into sys_user(`id`,`username`,`realname`,`password`,`salt`,`email`,`phone`,`org_code`,`status`,`del_flag`,`work_no`,`role_code`,`depart_ids`,`create_by`,`create_time`," \
              "`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s)"
        if len(result) == 0:
            data1 = ('a25462042f8a422f863ca93457fc3b94', 'jiangtest091201', '江华坤',
                     'de0b4c9bed5205767383ab28f47e9141', 'qzE2WhMK', None,
                     '13692659789', None, 1, 0, None,
                     'itri_all', None, 'jianghuakun', '2020-09-12 08:41:55', None,
                     None)
            db127.itri_ota_cursor.execute(sql, data1)
            db127.itri_ota.commit()
            #print("系统账户 插入数据成功")
        else:
            pass

            #print("系统账户 exit")
        #构造部门用户
        #构造部门用户-关联1个部门
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="jiang091201"')
        result1 =db127.itri_ota_cursor.fetchall()
        if len(result1)==0:
            data1=('741e7764fa4f4afc9fa6c61e1f9cac5c', 'jiang091201', 'jianghuakun', '9c3e4ec1f668a3dae515d5379b4d4f0a', 'zhg7Yl7o', None, '13692659859', None, 1, 0, None, 'itri_depart', '984bbb24e4614c6a9770d892c7d2fd54', 'jianghuakun', '2020-09-12 09:38:28', None,  None)
            db127.itri_ota_cursor.execute(sql,data1)
            db127.itri_ota.commit()

            #print("关联一个部门用户插入数据成功")
        else:
            pass
            #print("关联一个部门用户存在")

        #关联2个部门
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="09113"')
        result11 = db127.itri_ota_cursor.fetchall()
        if len(result11) == 0:
            data1 = ('6d13a2eb50be41abbed13926f88b391a', '09113', '09113',
                     'fd6014f4c2a543ba', 'avdHVAOZ', None,
                     '13547894563', None, 1, 0, None,
                     'itri_depart', '984bbb24e4614c6a9770d892c7d2fd54,5a98dcba815c49aea35dc199dde878c2', '09114', '2020-09-11 11:34:59', 'jianghuakun',
                     '2020-09-11 14:09:15')
            db127.itri_ota_cursor.execute(sql, data1)
            db127.itri_ota.commit()

            #print("关联一个部门用户插入数据成功")
        else:
            pass
            #print("关联一个部门用户存在")

        #部门用户编辑使用
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="091202"')
        result2 = db127.itri_ota_cursor.fetchall()
        if len(result2) == 0:
            data1 = ('be575b34bce14d32a044d7f6ff97f1bc', '091202', '江华坤',
                     'e927cc8569f709c3', 'WxAlntoI',None,
                     '13692659875', None, 1, 0, None,
                     'itri_depart', '984bbb24e4614c6a9770d892c7d2fd54', 'jianghuakun', '2020-09-12 09:53:46', None,
                     None)
            db127.itri_ota_cursor.execute(sql, data1)
            db127.itri_ota.commit()

            #print("关联一个部门用户插入数据成功")
        else:
            pass
            #print("关联一个部门用户存在")

        #部门用户验证2级部门只关联账户，不挂3级部门
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="09121738"')
        result21 = db127.itri_ota_cursor.fetchall()
        if len(result21) == 0:
            data1 = ('66ceb473b35c4819a5b997ecd1d99772', '09121738', '江华坤',
                     '9e79e61f97464acd306137dd3fe3f59a', 'dSQVFEYe', None,
                     '14878946587', None, 1, 0, None,
                     'itri_depart', '7d4c693baebe4278ad82fa072ee19924', 'jianghuakun', '2020-09-12 17:39:24', None,
                     None)
            db127.itri_ota_cursor.execute(sql, data1)
            db127.itri_ota.commit()

            # print("关联一个部门用户插入数据成功")
        else:
            pass
            # print("关联一个部门用户存在")

        #系统用户编辑删除使用
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="091203"')
        result3 = db127.itri_ota_cursor.fetchall()
        sql1 = "insert into sys_user(`id`,`username`,`realname`,`password`,`salt`,`email`,`phone`,`status`,`del_flag`,`work_no`,`role_code`,`create_by`,`create_time`,`update_by`,`update_time`) values( %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s,%s,%s, %s)"
        if len(result3) == 0:
            data1 = ('b366f059186347c69791e87d4de94e2d', '091203','江华坤','7f8183701bc79ec1', 'O7vDjSYj', None,'13692659876', None,1, 0,None,'itri_all',None,'jianghuakun', '2020-09-12 10:02:16', None,None)
            db127.itri_ota_cursor.execute(sql, data1)
            db127.itri_ota.commit()
            #print("系统账户 插入数据成功")
        else:
            pass

        #批量删除使用
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="江批量删除测试1"')
        result31 = db127.itri_ota_cursor.fetchall()
        #sql = "insert into sys_user(`id`,`username`,`realname`,`password`,`salt`,`email`,`phone`,`org_code`,`status`,`del_flag`,`work_no`,`role_code`,`create_by`,`create_time`,`update_by`,`update_time`) values( %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s)"
        if len(result31) == 0:
            data11 = ('3471e47a0f484aab8a93afea2ac5dc70', '江批量删除测试1', '江华坤',
                     '0963ae4c76bf0d4f50735529a26c5dcab24c929f87690465', 'Uv19wBEU', None,
                     '13691699128',None, 1, 0, None, 'itri_all',None,
                     'jianghuakun', '2020-09-07 11:10:44', None,
                     None)
            db127.itri_ota_cursor.execute(sql, data11)
            db127.itri_ota.commit()
            # print("系统账户 插入数据成功")
        else:
            pass

        #
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="江批量删除测试2"')
        result32 = db127.itri_ota_cursor.fetchall()
        #sql = "insert into sys_user(`id`,`username`,`realname`,`password`,`salt`,`email`,`phone`,`org_code`,`status`,`del_flag`,`work_no`,`role_code`,`create_by`,`create_time`,`update_by`,`update_time`) values( %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s)"
        if len(result32) == 0:
            data11 = ('6476a72861b840daaf064dd6377683aa', '江批量删除测试2', '江华坤',
                      'ae5335065ad4a119f2705353a5c16e9dc78fff007936a379', 'mdjdESUm', None,
                      '13691699129', None, 1, 0, None, 'itri_depart','984bbb24e4614c6a9770d892c7d2fd54',
                      'jianghuakun', '2020-09-07 11:12:14', None,
                      None)
            db127.itri_ota_cursor.execute(sql, data11)
            db127.itri_ota.commit()
            # print("系统账户 插入数据成功")
        else:
            pass
        #
        db127.itri_ota_cursor.execute('SELECT * FROM sys_user WHERE username="江批量删除测试3"')
        result33 = db127.itri_ota_cursor.fetchall()
        #sql = "insert into sys_user(`id`,`username`,`realname`,`password`,`salt`,`email`,`phone`,`org_code`,`status`,`del_flag`,`work_no`,`role_code`,`create_by`,`create_time`,`update_by`,`update_time`) values( %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s)"
        if len(result33) == 0:
            data11 = ('448e4731333b45ce9062ecb2f68387d7', '江批量删除测试3', '江华坤',
                      '99b5956018c621ed437e74073f87a5659f639ee5d7c00849', 'W4Bax0RO', None,
                      '13691691347', None, 1, 0, None, 'itri_depart', '984bbb24e4614c6a9770d892c7d2fd54', 'jianghuakun', '2020-09-07 11:13:13', None,
                      None)
            db127.itri_ota_cursor.execute(sql, data11)
            db127.itri_ota.commit()
            # print("系统账户 插入数据成功")
        else:
            pass

            #print("系统账户 exit")
        #print(123,len(result))
        # 构造部门用户-关联2个部门
        # 构造部门用户-关联3个部门
        #db127.itri_ota_cursor.close()
        #db127.itri_ota.close()
        return None

    def depart_create(self):
        # 构造部门，供创建部门账户使用
        #1级部门
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE id="efce7f79ee1447a2add33430c3b56240"')
        result51 = db127.itri_ota_cursor.fetchall()
        sql = "insert into sys_depart(`id`,parent_id,`depart_name`,`depart_name_en`,`depart_no`,`depart_order`,`org_type`,`org_code`,`mobile`,`fax`,`address`,`upgrade_type`,`status`,`del_flag`,`description`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s)"
        if len(result51) == 0:
            data5 = (
                'efce7f79ee1447a2add33430c3b56240', None, '江测试0907-1',
                '09071', None,0, 1, "A03",None,None,None,None, 1, 0,None,
                'jianghuakun', '2020-09-07 09:43:10', None,
                None)
            db127.itri_ota_cursor.execute(sql, data5)
            db127.itri_ota.commit()

            # print("2级部门3插入数据成功")
        else:
            pass
            # print("2级部门3存在")
        #对应2级部门1
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE id="984bbb24e4614c6a9770d892c7d2fd54"')
        result52 = db127.itri_ota_cursor.fetchall()
        #sql = "insert into sys_depart(`id`,parent_id,`depart_name`,`depart_name_en`,`depart_no`,`depart_order`,`org_type`,`org_code`,`mobile`,`fax`,`address`,`upgrade_type`,`status`,`del_flag`,`description`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s)"
        if len(result52) == 0:
            data5 = (
                '984bbb24e4614c6a9770d892c7d2fd54', 'efce7f79ee1447a2add33430c3b56240', '江测试2级部门0907-2',
                '090721', None, 0, 2, "A03A01", None, None, None, None, 1, 0, None,
                'jianghuakun', '2020-09-07 09:48:51', None,
                None)
            db127.itri_ota_cursor.execute(sql, data5)
            db127.itri_ota.commit()

            # print("2级部门3插入数据成功")
        else:
            pass
            # print("2级部门3存在")

        #对应部门2
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE id="5a98dcba815c49aea35dc199dde878c2"')
        result56 = db127.itri_ota_cursor.fetchall()
        # sql = "insert into sys_depart(`id`,parent_id,`depart_name`,`depart_name_en`,`depart_no`,`depart_order`,`org_type`,`org_code`,`mobile`,`fax`,`address`,`upgrade_type`,`status`,`del_flag`,`description`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s)"
        if len(result56) == 0:
            data5 = (
                '5a98dcba815c49aea35dc199dde878c2', 'efce7f79ee1447a2add33430c3b56240', '江测试2级部门2-2',
                '090822', None, 0, 2, "A03A02", None, None, None, None, 1, 0, None,
                'jianghuakun', '2020-09-08 17:54:36', None,
                None)
            db127.itri_ota_cursor.execute(sql, data5)
            db127.itri_ota.commit()

            # print("2级部门3插入数据成功")
        else:
            pass
            # print("2级部门3存在")

        #对应部门3
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE id="7d4c693baebe4278ad82fa072ee19924"')
        result57 = db127.itri_ota_cursor.fetchall()
        # sql = "insert into sys_depart(`id`,parent_id,`depart_name`,`depart_name_en`,`depart_no`,`depart_order`,`org_type`,`org_code`,`mobile`,`fax`,`address`,`upgrade_type`,`status`,`del_flag`,`description`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s)"
        if len(result57) == 0:
            data5 = (
                '7d4c693baebe4278ad82fa072ee19924', 'efce7f79ee1447a2add33430c3b56240', '江测试不挂3级部门只关联账户',
                '09121734', None, 0, 2, "A03A03", None, None, None, None, 1, 0, None,
                'jianghuakun', '2020-09-12 17:34:51', None,
                None)
            db127.itri_ota_cursor.execute(sql, data5)
            db127.itri_ota.commit()

            # print("2级部门3插入数据成功")
        else:
            pass
            # print("2级部门3存在")

        #部门1对应3级部门1
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE id="10611880139241048990bd5d7f4be58c"')
        result53 = db127.itri_ota_cursor.fetchall()
        # sql = "insert into sys_depart(`id`,parent_id,`depart_name`,`depart_name_en`,`depart_no`,`depart_order`,`org_type`,`org_code`,`mobile`,`fax`,`address`,`upgrade_type`,`status`,`del_flag`,`description`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s)"
        if len(result53) == 0:
            data5 = (
                '10611880139241048990bd5d7f4be58c', '984bbb24e4614c6a9770d892c7d2fd54', '江测试3级部门0907-3-1',
                'jiang090731', None, 0, 3, "A03A01A01", None, None, None, 1, 1, 0, None,
                'jianghuakun', '2020-09-07 10:33:08', None,
                None)
            db127.itri_ota_cursor.execute(sql, data5)
            db127.itri_ota.commit()

            # print("2级部门3插入数据成功")
        else:
            pass
            # print("2级部门3存在")

        #部门1对应3级部门2
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE id="f3ca5ddcd7f244d2b8f50af4c679363e"')
        result54 = db127.itri_ota_cursor.fetchall()
        # sql = "insert into sys_depart(`id`,parent_id,`depart_name`,`depart_name_en`,`depart_no`,`depart_order`,`org_type`,`org_code`,`mobile`,`fax`,`address`,`upgrade_type`,`status`,`del_flag`,`description`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s)"
        if len(result54) == 0:
            data5 = (
                'f3ca5ddcd7f244d2b8f50af4c679363e', '984bbb24e4614c6a9770d892c7d2fd54', '江测试产品0908-1',
                '090801', None, 0, 3, "A03A01A02", None, None, None, 0, 1, 0, None,
                'jianghuakun', '2020-09-08 13:57:20', None,
                None)
            db127.itri_ota_cursor.execute(sql, data5)
            db127.itri_ota.commit()

            # print("2级部门3插入数据成功")
        else:
            pass
            # print("2级部门3存在")

        #部门1对应3级部门3
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE id="b62c34673cdb4271b086c968a057f659"')
        result55 = db127.itri_ota_cursor.fetchall()
        # sql = "insert into sys_depart(`id`,parent_id,`depart_name`,`depart_name_en`,`depart_no`,`depart_order`,`org_type`,`org_code`,`mobile`,`fax`,`address`,`upgrade_type`,`status`,`del_flag`,`description`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s)"
        if len(result55) == 0:
            data5 = (
                'b62c34673cdb4271b086c968a057f659', '984bbb24e4614c6a9770d892c7d2fd54', '0909',
                '0909', None, 0, 3, "A03A01A03", None, None, None, 0, 1, 0, None,
                'jianghuakun', '2020-09-09 09:28:25', None,
                None)
            db127.itri_ota_cursor.execute(sql, data5)
            db127.itri_ota.commit()

            # print("2级部门3插入数据成功")
        else:
            pass
            # print("2级部门3存在")

        #部门2对应3级部门1
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE id="ac93835084904c048072df2120bb77fe"')
        result57 = db127.itri_ota_cursor.fetchall()
        # sql = "insert into sys_depart(`id`,parent_id,`depart_name`,`depart_name_en`,`depart_no`,`depart_order`,`org_type`,`org_code`,`mobile`,`fax`,`address`,`upgrade_type`,`status`,`del_flag`,`description`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s)"
        if len(result57) == 0:
            data5 = (
                'ac93835084904c048072df2120bb77fe', '5a98dcba815c49aea35dc199dde878c2', '江测试3级部门3-3',
                '090833', None, 0, 3, "A03A02A01", None, None, None, 0, 1, 0, None,
                'jianghuakun', '2020-09-08 17:57:42', None,
                None)
            db127.itri_ota_cursor.execute(sql, data5)
            db127.itri_ota.commit()

            # print("2级部门3插入数据成功")
        else:
            pass
            # print("2级部门3存在")

        #部门2对应3级部门2
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE id="5a1383f42a39436ca5abd59d9bf4600b"')
        result58 = db127.itri_ota_cursor.fetchall()
        # sql = "insert into sys_depart(`id`,parent_id,`depart_name`,`depart_name_en`,`depart_no`,`depart_order`,`org_type`,`org_code`,`mobile`,`fax`,`address`,`upgrade_type`,`status`,`del_flag`,`description`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s,%s, %s, %s, %s,%s,%s, %s)"
        if len(result58) == 0:
            data5 = (
                '5a1383f42a39436ca5abd59d9bf4600b', '5a98dcba815c49aea35dc199dde878c2', '090902',
                '090902', None, 0, 3, "A03A02A02", None, None, None, 0, 1, 0, None,
                'jianghuakun', '2020-09-09 10:58:10', None,
                None)
            db127.itri_ota_cursor.execute(sql, data5)
            db127.itri_ota.commit()

            # print("2级部门3插入数据成功")
        else:
            pass
            # print("2级部门3存在")

        #构造1级部门
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="jiang-autotest-1级部门"')
        result1 = db127.itri_ota_cursor.fetchall()
        sql1 = "insert into sys_depart(`id`,`depart_name`,`depart_name_en`,`depart_order`,`org_type`,`org_code`,`status`,`del_flag`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"

        if len(result1) == 0:
            data1 = ('500f1e534cfc4a5c8336de71123f0c83', 'jiang-autotest-1级部门', 'jiangautotest1',0,1,"A90",1,0, 'itriota', '2020-07-31 08:28:12', 'itriota',
                     '2020-07-31 08:28:12')
            db127.itri_ota_cursor.execute(sql1, data1)
            db127.itri_ota.commit()
            #print("1级部门 插入数据成功")
        else:
            pass

            #print("1级部门 exit")

        #不关联账户和2级部门

        #构造2级部门1
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="jiang-autotest-2级部门-1"')
        result2 =db127.itri_ota_cursor.fetchall()
        sql2 = "insert into sys_depart(`id`,`parent_id`,`depart_name`,`depart_name_en`,`depart_order`,`org_type`,`org_code`,`status`,`del_flag`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s,%s,%s,%s)"
        print(result2)
        if len(result2)==0:
            data2 = ('b724b422e68945ff8f3f1dc7997d06f4','500f1e534cfc4a5c8336de71123f0c83','jiang-autotest-2级部门-1', 'jiangautotest21',None, 0, 2, "A90A01", None, None, None, None, 1, 0,None,
                     'itriota', '2020-07-31 08:31:52', 'itriota',
                     '2020-07-31 08:31:52')
            db127.itri_ota_cursor.execute(sql,data2)
            db127.itri_ota.commit()

            #print("2级部门1插入数据成功")
        else:
            pass
            #print("2级部门1存在")
        # 构造2级部门2
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="jiang-autotest-2级部门-2"')
        result3 = db127.itri_ota_cursor.fetchall()
        sql3 = "insert into sys_depart(`id`,`parent_id`,`depart_name`,`depart_name_en`,`depart_order`,`org_type`,`org_code`,`status`,`del_flag`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s)"
        if len(result3) == 0:
            data3 = ('4ba6ade2f0c54f668b64392120b5c80d', '500f1e534cfc4a5c8336de71123f0c83', 'jiang-autotest-2级部门-2',
                     'jiangautotest22', 0, 2, "A90A02", 1, 0,
                     'itriota', '2020-07-31 08:31:52', 'itriota',
                     '2020-07-31 08:31:52')
            db127.itri_ota_cursor.execute(sql3,data3)
            db127.itri_ota.commit()

            #print("2级部门2插入数据成功")
        else:
            pass
            #print("2级部门2存在")
        # 构造2级部门3
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="jiang-autotest-2级部门-3"')
        result4 = db127.itri_ota_cursor.fetchall()
        sql4 = "insert into sys_depart(`id`,`parent_id`,`depart_name`,`depart_name_en`,`depart_order`,`org_type`,`org_code`,`status`,`del_flag`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s,%s, %s, %s)"
        if len(result4) == 0:
            data4 = (
                '4ec536de450c44ab848ce3b1c1725442', '500f1e534cfc4a5c8336de71123f0c83', 'jiang-autotest-2级部门-3',
                'jiangautotest23', 0, 2, "A90A03", 1, 0,
                'itriota', '2020-07-31 08:32:07', 'itriota',
                '2020-07-31 08:32:07')
            db127.itri_ota_cursor.execute(sql4, data4)
            db127.itri_ota.commit()

            #print("2级部门3插入数据成功")
        else:
            pass
            #print("2级部门3存在")
        #构造3级部门1

        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE id="1ec219ce8ec94fb4b2055b15ae054e6e"')
        result5 = db127.itri_ota_cursor.fetchall()
        sql5 = "insert into sys_depart(`id`,parent_id,`depart_name`,`depart_name_en`,`depart_order`,`org_type`,`org_code`,`upgrade_type`,`status`,`del_flag`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s,%s, %s)"
        if len(result5) == 0:
            data5 = (
                '1ec219ce8ec94fb4b2055b15ae054e6e', '4ba6ade2f0c54f668b64392120b5c80d', 'jiang-autotest-3级部门-1',
                'jiangautotest31', 0, 3, "A90A02A01",1, 1, 0,
                'itriota', '2020-07-31 08:40:09', 'itriota',
                '2020-07-31 08:40:09')
            db127.itri_ota_cursor.execute(sql5, data5)
            db127.itri_ota.commit()

            #print("2级部门3插入数据成功")
        else:
            pass
            #print("2级部门3存在")

        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE id="41159ee1c7c2405680963e41315ed6f5"')
        result51 = db127.itri_ota_cursor.fetchall()
        sql51 = "insert into sys_depart(`id`,parent_id,`depart_name`,`depart_name_en`,`depart_order`,`org_type`,`org_code`,`upgrade_type`,`status`,`del_flag`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s,%s, %s)"
        if len(result51) == 0:
            data51 = (
                '41159ee1c7c2405680963e41315ed6f5', '4ba6ade2f0c54f668b64392120b5c80d', 'jiang-autotest-3级部门-2',
                'jiangautotest32', 0, 3, "A90A02A02",0, 1, 0,
                'itriota', '2020-08-10 09:03:48', 'itriota',
                '2020-08-10 09:03:48')
            db127.itri_ota_cursor.execute(sql51, data51)
            db127.itri_ota.commit()

            #print("2级部门3插入数据成功")
        else:
            pass
            #print("2级部门3存在")

        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE id="e2429e3841604e10880dc10b02e088c2"')
        result52 = db127.itri_ota_cursor.fetchall()
        sql52 = "insert into sys_depart(`id`,parent_id,`depart_name`,`depart_name_en`,`depart_order`,`org_type`,`org_code`,`upgrade_type`,`status`,`del_flag`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s,%s, %s)"
        if len(result52) == 0:
            data52 = (
                'e2429e3841604e10880dc10b02e088c2','4ec536de450c44ab848ce3b1c1725442','jiang-autotest-3级部门-3','jiangautotest33',0,3,"A90A03A01",1,1,0,'itriota','2020-08-10 09:14:04','itriota','2020-08-10 09:14:048')
            db127.itri_ota_cursor.execute(sql52, data52)
            db127.itri_ota.commit()

            #print("2级部门3插入数据成功")
        else:
            pass
            #print("2级部门3存在")
        #print(123,len(result))
        # 构造部门用户-关联2个部门
        # 构造部门用户-关联3个部门
        #db127.itri_ota_cursor.close()
        #db127.itri_ota.close()

        #不关联任何账户和挂子部门
        #1.1级部门
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="jiang-autotest-1级部门2"')
        result6 = db127.itri_ota_cursor.fetchall()
        sql6 = "insert into sys_depart(`id`,`depart_name`,`depart_name_en`,`depart_order`,`org_type`,`org_code`,`status`,`del_flag`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"
        if len(result6) == 0:
            data6 = (
                'dcb15304b45a483c8d640235704c9626', 'jiang-autotest-1级部门2', 'jiangautotest12', 0, 1, "A10", 1, 0,
                'itriota',
                '2020-08-03 14:36:59', 'itriota',
                '2020-08-03 14:36:59')
            db127.itri_ota_cursor.execute(sql6, data6)
            db127.itri_ota.commit()
            #print("系统账户 插入数据成功")
        else:
            pass

            #print("系统账户 exit")

        #2.2级部门
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="jiang-autotest-2级部门-4"')
        result7 = db127.itri_ota_cursor.fetchall()
        sql7 = "insert into sys_depart(`id`,`parent_id`,`depart_name`,`depart_name_en`,`depart_order`,`org_type`,`org_code`,`status`,`del_flag`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,%s, %s, %s, %s,%s,%s, %s, %s, %s)"
        if len(result7) == 0:
            data7 = (
                '494672e1b5b441b9b2f1edf6b78d17cd', '500f1e534cfc4a5c8336de71123f0c83', 'jiang-autotest-2级部门-4',
                'jiangautotest24', 0, 2, "A90A05", 1, 0,
                'itriota',
                '2020-08-03 14:47:51', 'itriota',
                '2020-08-03 14:47:51')
            db127.itri_ota_cursor.execute(sql7, data7)
            db127.itri_ota.commit()
            #print("系统账户 插入数据成功")
        else:
            pass

            #print("系统账户 exit")

        #3.3级部门
        db127.itri_ota_cursor.execute('SELECT * FROM sys_depart WHERE depart_name="jiang-autotest-3级部门-2"')
        result8 = db127.itri_ota_cursor.fetchall()
        sql8 = "insert into sys_depart(`id`,`parent_id`,`depart_name`,`depart_name_en`,`depart_order`,`org_type`,`org_code`,`upgrade_type`,`status`,`del_flag`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s, %s,  %s,%s, %s, %s, %s,%s, %s,%s, %s, %s)"
        if len(result8) == 0:
            data8 = (
                '41159ee1c7c2405680963e41315ed6f5', '4ba6ade2f0c54f668b64392120b5c80d', 'jiang-autotest-3级部门-2',
                'jiangautotest32', 0, 3, "A90A02A02", 1,1, 0,
                'itriota',
                '2020-08-03 14:58:21', 'itriota',
                '2020-08-03 14:58:21')
            db127.itri_ota_cursor.execute(sql8, data8)
            db127.itri_ota.commit()
            #print("系统账户 插入数据成功")
        else:
            pass

            #print("系统账户 exit")

        return None
    def oss_file_create(self):
        sql = "insert into t_oss_file(`id`, `depart_id`,`file_type`,`file_name`,`app_package_name`,`version`,`size`,`md5`,`url`,`create_by`,`create_time`) values(%s, %s,%s, %s, %s, %s,%s, %s,%s, %s, %s)"
        db127.itri_ota_cursor.execute('SELECT * FROM t_oss_file WHERE id="02f2f6b9c4f4447b8d6cf3e6eccf7708"')
        result=db127.itri_ota_cursor.fetchall()

        # 新增文件记录1
        if len(result)==0:
            data = (
                '02f2f6b9c4f4447b8d6cf3e6eccf7708', '1ec219ce8ec94fb4b2055b15ae054e6e', 0,
                'com.bmwxzpj.apk', "baimao2.8", "2.8", 12339036, "680839d893dd923a9f8ed9aecb34584d", "https://fenda-itri-t1-830.oss-cn-shenzhen.aliyuncs.com/jiangtest3/jiangnomobile15/jiangtestsetoss/app/2.8/1594799897764-69900ce7ad5343bd9f64c13f0e84ad1c.apk",
                'jiangtestdepend_1-1',
                '2020-08-07 10:58:20')
            db127.itri_ota_cursor.execute(sql, data)
            db127.itri_ota.commit()
            #print("系统账户 插入数据成功")
        else:
            pass

        db127.itri_ota_cursor.execute('SELECT * FROM t_oss_file WHERE id="793f419f22954f3eab09129c6bff2dd6"')
        result1 = db127.itri_ota_cursor.fetchall()

        # 新增文件记录2
        if len(result1) == 0:
            data1 = (
                '793f419f22954f3eab09129c6bff2dd6', '1ec219ce8ec94fb4b2055b15ae054e6e', 0,
                'com.DemoApp.apk', "demo3.1", "3.1", 29466980, "2bb4a4e17cf6aa520baa615cf8df05be",
                "https://fenda-itri-t1-830.oss-cn-shenzhen.aliyuncs.com/jiangtest3/jiangnomobile15/jiangtestsetoss/app/3.1/1594801299911-0032779213fe42df852628a1a22ff0e5.apk",
                'jiangtestdepend_1-1',
                '2020-08-07 09:21:47')
            db127.itri_ota_cursor.execute(sql, data1)
            db127.itri_ota.commit()
            #print("系统账户 插入数据成功")
        else:
            pass
        #新增文件记录3
        db127.itri_ota_cursor.execute('SELECT * FROM t_oss_file WHERE id="d9fb3fe973e94409b6dee1084c88e04e"')
        result1 = db127.itri_ota_cursor.fetchall()

        if len(result1) == 0:
            data1 = (
                'd9fb3fe973e94409b6dee1084c88e04e', '1ec219ce8ec94fb4b2055b15ae054e6e', 1,
                'com.bmwxzpj.apk', "t2.4", "1.0", 12062677, "8bfb3fe7312f0f51845dc2f857c30fca",
                "https://fenda-itri-t1-830.oss-cn-shenzhen.aliyuncs.com/jiangtest3/jiangnomobile15/jiangtestsetoss/firware/1.0/1594950668311-ddf362786a3844cc9472b58d4655ae21.zip",
                'itriota',
                '2020-08-07 09:51:11')
            db127.itri_ota_cursor.execute(sql, data1)
            db127.itri_ota.commit()
            #print("系统账户 插入数据成功")
        else:
            pass

        # 新增文件记录4
        db127.itri_ota_cursor.execute('SELECT * FROM t_oss_file WHERE id="3b94aedd2dc44a2ebb13bdfc83d20338"')
        result1 = db127.itri_ota_cursor.fetchall()

        if len(result1) == 0:
            data1 = (
                '3b94aedd2dc44a2ebb13bdfc83d20338', 'e2429e3841604e10880dc10b02e088c2', 0,
                 "keep",None, "2.1", 54132957, "d34e7f63adcd973052ddd3ab3e47d503",
                "https://fenda-itri-t1-830.oss-cn-shenzhen.aliyuncs.com/jiangnoaddress12/jiangnodepartNo1/jiangtestsetpswd315/app/2.1/1594949279048-d9107d3734c84c5bb14c1c1aa9ddf1eb.apk",
                'itriota',
                '2020-07-17 09:28:14')
            db127.itri_ota_cursor.execute(sql, data1)
            db127.itri_ota.commit()
            #print("系统账户 插入数据成功")
        else:
            pass

        # 新增文件记录5
        db127.itri_ota_cursor.execute('SELECT * FROM t_oss_file WHERE id="3b94aedd2dc44a2ebb13bdfc83d20339"')
        result1 = db127.itri_ota_cursor.fetchall()

        if len(result1) == 0:
            data1 = (
                '3b94aedd2dc44a2ebb13bdfc83d20339', 'f3ca5ddcd7f244d2b8f50af4c679363e', 0,
                 "keep1",None, "22.1", 54132957, "d34e7f63adcd973052ddd3ab3e47d504",
                "https://fenda-itri-t1-830.oss-cn-shenzhen.aliyuncs.com/jiangnoaddress12/jiangnodepartNo1/jiangtestsetpswd315/app/2.1/1594949279048-d9107d3734c84c5bb14c1c1aa9ddf1eb.apk",
                'itriota',
                '2020-07-17 09:28:14')
            db127.itri_ota_cursor.execute(sql, data1)
            db127.itri_ota.commit()
            # print("系统账户 插入数据成功")
        else:
            pass
        # 新增文件记录5
        db127.itri_ota_cursor.execute('SELECT * FROM t_oss_file WHERE id="3b94aedd2dc44a2ebb13bdfc83d20340"')
        result1 = db127.itri_ota_cursor.fetchall()

        if len(result1) == 0:
            data1 = (
                '3b94aedd2dc44a2ebb13bdfc83d20340', 'f3ca5ddcd7f244d2b8f50af4c679363e', 0,
                 "keep2",None, "222.1", 54132957, "d34e7f63adcd973052ddd3ab3e47d505",
                "https://fenda-itri-t1-830.oss-cn-shenzhen.aliyuncs.com/jiangnoaddress12/jiangnodepartNo1/jiangtestsetpswd315/app/2.1/1594949279048-d9107d3734c84c5bb14c1c1aa9ddf1eb.apk",
                'itriota',
                '2020-07-17 09:28:14')
            db127.itri_ota_cursor.execute(sql, data1)
            db127.itri_ota.commit()
            # print("系统账户 插入数据成功")
        else:
            pass


    #新增版本
    def version_create(self):
        sql = "insert into t_version(`id`, `task_name`,`version`,`depart_id`,`file_id`,`changle_log`,`source`,`limit_number`,`version_whitelist`,`user_group_ids`,`network_type`,`force_flag`,`battery_threshold`,`status`,`del_flag`,`description`,`create_by`,`create_time`,`update_by`,`update_time`) values( %s,%s, %s,%s, %s, %s, %s,%s, %s,%s, %s, %s, %s, %s, %s,%s, %s,%s, %s, %s)"
        db127.itri_ota_cursor.execute('SELECT * FROM t_version WHERE id="07e4f3cb685749bcac2951beef6bc940"')
        result=db127.itri_ota_cursor.fetchall()

        # 新增版本1
        if len(result)==0:
            data = (
                '07e4f3cb685749bcac2951beef6bc940', 'keep1.0',"2.8","1ec219ce8ec94fb4b2055b15ae054e6e","02f2f6b9c4f4447b8d6cf3e6eccf7708","2.8", 0,0,
                None,None, 0,0,"60%", 1,0,"2.8", "itriota", "2020-08-10 08:41:10", "itriota", "2020-08-10 08:41:10")
            db127.itri_ota_cursor.execute(sql, data)
            db127.itri_ota.commit()
            #print("系统账户 插入数据成功")
        else:
            pass

        #sql = "insert into t_version(`id`, `task_name`,`version`,`depart_id`,`file_id`,`changle_log`,`source`,`upgrade_type`,`limit_number`,`version_whitelist`,`user_whitelist`,`network_type`,`battery_threshold`,`status`,`del_flag`,`description`,`create_by`,`create_time`,`update_by`,`update_time`) values(%s, %s, %s,%s, %s, %s, %s,%s, %s,%s, %s, %s, %s, %s, %s,%s, %s,%s, %s, %s)"
        db127.itri_ota_cursor.execute('SELECT * FROM t_version WHERE id="116109ea9aa24597acaf684454bb6eea"')
        result = db127.itri_ota_cursor.fetchall()

        # 新增版本2
        if len(result) == 0:
            data = (
                '116109ea9aa24597acaf684454bb6eea', 't2.4', "1.0", "e2429e3841604e10880dc10b02e088c2",
                "3b94aedd2dc44a2ebb13bdfc83d20338", "t2.4", 0, 0,
                None, None, 1, 0,"60%", 1, 0, "3.1", "itriota", "2020-08-11 10:28:03", "itriota", "2020-08-11 10:28:03")
            db127.itri_ota_cursor.execute(sql, data)
            db127.itri_ota.commit()
            # print("系统账户 插入数据成功")
        else:
            pass

        # 新增版本3
        db127.itri_ota_cursor.execute('SELECT * FROM t_version WHERE id="116109ea9aa24597acaf684454bb6eeb"')
        result = db127.itri_ota_cursor.fetchall()
        if len(result) == 0:
            data = (
                '116109ea9aa24597acaf684454bb6eeb', 't22.4', "1.0", "f3ca5ddcd7f244d2b8f50af4c679363e",
                "3b94aedd2dc44a2ebb13bdfc83d20339", "t2.4", 0, 0,
                None, None, 1, 0,"60%", 1, 0, "3.1", "itriota", "2020-08-11 10:28:03", "itriota", "2020-08-11 10:28:03")
            db127.itri_ota_cursor.execute(sql, data)
            db127.itri_ota.commit()
            # print("系统账户 插入数据成功")
        else:
            pass

        db127.itri_ota_cursor.execute('SELECT * FROM t_version WHERE id="116109ea9aa24597acaf684454bb6eec"')
        result = db127.itri_ota_cursor.fetchall()
        if len(result) == 0:
            data = (
                '116109ea9aa24597acaf684454bb6eec', 't22.41', "11.0", "f3ca5ddcd7f244d2b8f50af4c679363e",
                "3b94aedd2dc44a2ebb13bdfc83d20340", "t21.4", 0, 0,
                None, None, 1, 0, "60%", 1, 0, "3.1", "itriota", "2020-08-11 10:28:03", "itriota",
                "2020-08-11 10:28:03")
            db127.itri_ota_cursor.execute(sql, data)
            db127.itri_ota.commit()
            # print("系统账户 插入数据成功")
        else:
            pass
    #新增用户白名单
    def user_group_create(self):
        sql = "insert into t_user_group(`id`, `group_name`,`user_whilelist`,`depart_id`,`description`,`create_by`,`create_time`,`update_by`,`update_time`) values( %s,%s, %s,%s, %s, %s, %s,%s, %s)"
        db127.itri_ota_cursor.execute('SELECT * FROM t_user_group WHERE id="0b586090ab6d47898138caba99018e51"')
        result=db127.itri_ota_cursor.fetchall()

        # 新增白名单1
        if len(result)==0:
            data = (
                '0b586090ab6d47898138caba99018e51', '818',"123","e2429e3841604e10880dc10b02e088c2",None,"jiangtestdepend_1-2", "2020-08-25 11:15:51", "jiangtestdepend_1-2", "2020-08-25 11:15:50")
            db127.itri_ota_cursor.execute(sql, data)
            db127.itri_ota.commit()
            #print("系统账户 插入数据成功")
        else:
            pass

        # 新增白名单2
        db127.itri_ota_cursor.execute('SELECT * FROM t_user_group WHERE id="a63433af85ad46e8864dc5e5e77505a5"')
        result1 = db127.itri_ota_cursor.fetchall()


        if len(result1) == 0:
            data = (
                'a63433af85ad46e8864dc5e5e77505a5', '819', "819", "e2429e3841604e10880dc10b02e088c2", None,
                "jiangtestdepend_1-2", "2020-08-25 11:15:51", "jiangtestdepend_1-2", "2020-08-25 11:15:50")
            db127.itri_ota_cursor.execute(sql, data)
            db127.itri_ota.commit()
            # print("系统账户 插入数据成功")
        else:
            pass

        # 新增白名单3
        db127.itri_ota_cursor.execute('SELECT * FROM t_user_group WHERE id="3ffc49cf96ef4ef0a7659b049bd4b3d2"')
        result1 = db127.itri_ota_cursor.fetchall()


        if len(result1) == 0:
            data = (
                '3ffc49cf96ef4ef0a7659b049bd4b3d2', 'userwhiteauto1942', "123,456", "f3ca5ddcd7f244d2b8f50af4c679363e", None,
                "jianghuakun", "2020-09-14 19:42:48", None, None)
            db127.itri_ota_cursor.execute(sql, data)
            db127.itri_ota.commit()
            # print("系统账户 插入数据成功")
        else:
            pass

        # 新增白名单4
        db127.itri_ota_cursor.execute('SELECT * FROM t_user_group WHERE id="24527662dc424e11b055900ffc80f2a1"')
        result1 = db127.itri_ota_cursor.fetchall()


        if len(result1) == 0:
            data = (
                '24527662dc424e11b055900ffc80f2a1', '0908', "0908", "f3ca5ddcd7f244d2b8f50af4c679363e",
                "0908",
                "jianghuakun", "2020-09-14 19:42:48", None, None)
            db127.itri_ota_cursor.execute(sql, data)
            db127.itri_ota.commit()
            # print("系统账户 插入数据成功")
        else:
            pass





