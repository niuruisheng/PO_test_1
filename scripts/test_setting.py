# 检索项目中的文件，每个引用自己本地封装代码，都需要添加
import os, sys
sys.path.append(os.getcwd())

from appium import webdriver
from base.base_driver import init_driver
from page.display_page import DisplayPage


class TestSetting:

    def test_setup(self):
        self.driver = init_driver()
    def test_display(self):
        self.display_page.clich_display()
        self.display_page.clich_wode()
