import time
from selenium.webdriver.support.wait import WebDriverWait
from config.conf import ConfYaml
from utils.driverutil import DriverUtil


class Base(object):
    def __init__(self):
        self.driver = DriverUtil.get_driver(ConfYaml().get_config_url()['url_warehouse'])

    # 查找元素方法
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()  # 输入前清空
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H-%M-%S")))

    # 判断元素是否存在封装
    def base_element_if_exit(self, loc):
        try:
            self.base_find_element(loc, timeout=2)  # 假如找登陆按钮，则需要先退出，如果退出是失败的，则需要等待30秒，这种情况下直接指定2秒，无需等待待太久
            return True
        except:
            return False