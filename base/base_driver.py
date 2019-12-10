# coding = utf-8
from appium import webdriver

def init_driver():
    #   server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = '9YEDU18427050342'
    desired_caps['automationName'] = 'UiAutomator2'
    # app信息
    # desired_caps['appPackage'] = 'com.sinopec.ejoyoil'
    # desired_caps['appActivity'] = 'com.sinopec.ejoyoil.mvp.splash.SplashActivity'
    desired_caps['appPackage'] = 'com.beijingshiyou.APP123'
    desired_caps['appActivity'] = 'com.beijingshiyou.APP123.mvp.splash.SplashActivity'
    # 中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明对象
    driver = webdriver.Remote( 'http://127.0.0.1:4723/wd/hub', desired_caps )
    return driver