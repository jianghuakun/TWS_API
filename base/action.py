
import os
import config
from selenium import webdriver
class Action:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def do_action(self,data):
        try:
            if data["动作"] == "断言":
                text = self.driver.get_element(data["定位类型"] + '=>' + data["定位值"]).text
                return text
            if data["动作"] == "打开":
                self.driver.get(data["输入值"])
            if data["动作"] == "点击":
                self.driver.find_elements_by_xpath("%s"%(data["action_type"],)).click()
            if data["动作"] == "清除":
                self.driver.clear(data["定位类型"] + '=>' + data["定位值"])

            # if data["动作"] == "等待":
            #     self.driver.wait(int(data["输入值"]))

            if data["动作"] == "输入":
                self.driver.type(data["定位类型"] + '=>' + data["定位值"],data["输入值"])
            if data["动作"] == "滚动条下拉":
                self.driver.js( "var q=document.body.scrollTop="+data["输入值"]+";")
            if data["动作"] == "等待元素":
                self.driver.element_wait(data["定位类型"] + '=>' + data["定位值"],10)
            if data["动作"] == "最大化":
                self.driver.max_window()
            if data["动作"] == "关闭浏览器":
                self.driver.close()
            if data["动作"] == "外调程序":
                os.system(data["输入值"])
        except Exception as e :
            Pylog.error("异常截图-"+data["动作"]+str(e))
            self.driver.save_png('./Report/'+data['用例No']+'.jpg')