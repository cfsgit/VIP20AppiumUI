from appium import webdriver
import time


def startup():
    print('开始启动')
    desire_caps = {
        'deviceName': '127.0.0.1:21503',
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        'appPackage': 'com.ss.android.article.news',
        'appActivity': 'com.ss.android.article.news.activity.MainActivity',
        'noReset': True,
        'unicodeKeyboard': True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
    print('启动成功，等待6s')
    time.sleep(6)


if __name__ == '__main__':
    startup()
