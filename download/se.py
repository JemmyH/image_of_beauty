# from selenium import webdriver
# import os
# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# brower = webdriver.Chrome(chromedriver)
# page = brower.get("http://xgyw.tpzy5.com/uploadfile/201805/8/5C223025472.jpg")
# print(page)
import os
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys as k
from selenium.webdriver.common.action_chains import ActionChains as ac
# import win32api
# import wn32con

def wb():
    a = wd.Firefox()
    a.get("http://xgyw.tpzy5.com/uploadfile/201805/8/5C223025472.jpg")
    element = a.find_element_by_xpath("/html/body/img")
    action = ac(a).context_click(element)
    action.send_keys_to_element(element,"v")
    action.perform()

def qi(url):
    pass
if __name__ == '__main__':
    # print(os.path)
    # wb()
    qi("http://xgyw.tpzy5.com/uploadfile/201805/8/60222523906.jpg")
