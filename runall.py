import time

from appium import webdriver
from selenium.webdriver.common.by import By


def startup():
    print('准备启动')
    desired_caps = {
        "deviceName": "127.0.0.1:21503",
        "platformName": "Android",
        "platformVersion": "5.1.1",  # 所连接设备的系统版本
        "appPackage": "com.ss.android.article.news",
        "appActivity": "com.ss.android.article.news.activity.MainActivity",
        "noReset": True,
        "unicodeKeyboard": True

    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    print('启动成功，等待3s')
    time.sleep(3)

    # resource-id 写法，定位发布按钮
    # driver.find_element(By.ID, 'com.ss.android.article.news:id/bpx')  # 定位
    # driver.find_element(By.ID, 'com.ss.android.article.news:id/bpx').click()  # 定位+操作
    # time.sleep(2)
    # assert '文章' in driver.page_source
    # print('有文章')
    # 断言
    # driver.find_elements(By.ID, 'com.ss.android.article.news:id/bxm')[1].click()  # 点击 文章
    # time.sleep(3)  # 加入等待时间，如果不加等待时间  下方的的标题元素则无法定位   会报错
    # driver.find_element_by_class_name("android.widget.EditText").send_keys('你好，这是今日头条标题')  # 添加标题文本内容
    # driver.find_element_by_class_name("android.view.View").send_keys('你好，这是今日头条内容')  # 添加文本内容
    # driver.find_element(By.ID, 'com.ss.android.article.news:id/b0z').click()  # 右上角发布按钮

    # driver.tap([(100, 200)])  # driver.tap([坐标]，持续点击时间)，除了定位到元素的点击外，也可以通过 tab 实现坐标的点击
    # windowsSiz = driver.get_window_size()  # 获取屏幕的尺寸
    # size = getsize(driver)
    #
    # print(f"屏幕的尺寸：{size}")  # 打印屏幕的尺寸
    # swipeUp(driver)
    driver.close_app()  #相当于关闭页面
    print('关闭app')
    time.sleep(5)
    driver.launch_app()
    time.sleep(3)
    print('启动app')
    driver.quit()   # 杀死进程


def getsize(driver):  # 获取屏幕尺寸
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


def swipeUp(driver, t=1000):  # 向上滑动
    l = getsize(driver)
    x1 = l[0] * 0.5  # x 坐标
    y1 = l[1] * 0.75  # y1 开始坐标
    y2 = l[1] * 0.25  # y2 结束坐标
    driver.swipe(x1, y1, x1, y2, t)
    print('完成上滑')


if __name__ == '__main__':
    startup()
