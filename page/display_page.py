from



class DisplayPage:

    def __init__(self,driver):
        self.driver = driver
        # 显示一级页面，同一页面
        # （init里面可以去写已经确定的这个模块所有的前置功能）
        self.clich_display()

    def clich_display(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]").click()
        # self.driver.find_element(By.XPATH.).clich()

    # def find_element(self,loc):
    #     self.driver.find_element(loc[0],loc[1])
    # 进入我的页面
    def clich_wode(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="我的"]/android.view.ViewGroup/android.widget.TextView').click()
    # 点击登录注册
    def clich_shuru(self):
        self.driver.find_element_by_id("com.beijingshiyou.APP123:id/tv_username").click()
    # 登录页面，点击允许
    def clich_yunxu(self):
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    # 点击账号密码登录
    def clich_mimadeng(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.ImageView").click()
    # 录入登录信息
    def clich_zhanghao(self):
        self.driver.find_element_by_id("com.beijingshiyou.APP123:id/et_phone").send_keys("13520180391")
        self.driver.find_element_by_id("com.beijingshiyou.APP123:id/et_pwd").send_keys("aa1234")
        self.driver.find_element_by_id("com.beijingshiyou.APP123:id/btn_login").clich()



