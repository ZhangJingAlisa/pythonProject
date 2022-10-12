from selenium import webdriver
from time import sleep

# 导入此包为使用显示等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 鼠标操作
from selenium.webdriver.common.action_chains import ActionChains

# 键盘操作
from selenium.webdriver.common.keys import Keys

# 下拉框
from selenium.webdriver.support.select import Select

# 打开百度网址
driver = webdriver.Chrome()
url = "https://www.baidu.com/"
driver.get(url)

# 定位元素并输入内容，还可以通过name,tag_name,class_name等查询
# send_keys表示输入内容
# driver.find_element_by_id("kw").send_keys("美女")
# driver.find_element_by_name("wd")
# driver.find_element_by_tag_name("input")
# driver.find_element_by_class_name("s_ipt")

# 定位元素并点击按钮
# driver.find_element_by_id("su").click()

# 定位到某个a标签
# driver.find_element_by_link_text("hao123").click()
# 也是定位a标签，但是可以通过部分文字定位，像like
# driver.find_element_by_partial_link_text("hao123").click()

# 通过css选择器定位
# driver.find_element_by_css_selector(".s_ipt").send_keys("美女")
# driver.find_element_by_css_selector("[value=百度一下]").click()  #可以通过任意属性进行定位

# xpath：xml（可扩展标记语言：extensible Markup language） path
# html: hyper text markup language
# 复制xpath：右键检查，选中对应标签，右键选择Copy，再选择Copy XPath即可
# driver.find_element_by_xpath("//*[@id='kw']")

# 元素操作
# clear()  清除文本
# send_keys()  模拟输入
# click()  单击元素

# 元素属性
# size  获取元素大小
# text  获取元素文本
# get_attribute()  获取属性值
# is_display()  判断元素是否可见
# is_enabled()  判断元素是否可用
# print(driver.find_element_by_id("kw").size)
# print(driver.find_element_by_id("kw").text)
# print(driver.find_element_by_id("kw").get_attribute("name"))
# print(driver.find_element_by_id("kw").is_displayed())
# print(driver.find_element_by_id("kw").is_enabled())

# 浏览器的操作
# driver.maximize_window()  #最大化浏览器窗口
# driver.set_window_size(1920,1080)   #设置浏览器宽高
# driver.set_window_position(200,200)  #设置浏览器位置
# driver.back() #后退
# driver.forward()  #前进
# driver.refresh()  #刷新
# driver.close()  #关闭当前页面
# driver.quit()  #关闭浏览器

# 浏览器信息（属性）
# driver.title  #获取页面title
# driver.current_url  #获取当前页面url

# 等待
  # 代码的执行速度，远远快于页面的加载速度，在翻页的时候，或者是在加载新的页面的时候，需要进行页面等待
  # 页面的等待方式有三种：
  # 1、强制等待  sleep
  # 2、显示等待
  # 3、隐式等待   推荐

# 显示等待某个元素加载完成，每隔0.5秒检查一次，最多等待5秒
# WebDriverWait(driver,5).until(EC.presence_of_element_located((By.xpath), "//*[@id=1]/div/h3/a"))

# 隐式等待
# driver.implicitly_wait(5)
# driver.find_element_by_xpath("//*[@id=1]/div/h3/a").click()

# 鼠标操作
#     1、创建ActionChains对象
#     2、使用ActionChains对象的方法，进行操作
#     3、常用：
#         context_click()  鼠标右击
#         double_click()  鼠标双击
#         drag_and_drop()  鼠标拖动
#         move_to_element()  鼠标悬停
#     4、通过ActionChains“提交”这些操作
#         perform() 执行（用于执行以上所有鼠标方法）
# chians = ActionChains(driver)
# # chians.context_click(driver.find_element_by_id("su"))
# chians.move_to_element(driver.find_element_by_class_name("soutu-btn"))
# # 执行事件
# chians.perform()

# 键盘操作
# element.send_keys()
# el = driver.find_element_by_id("kw")
# el.send_keys("python")
# sleep(2)
# el.send_keys(Keys.CONTROL,"a")  #全选
# sleep(2)
# el.send_keys(Keys.BACK_SPACE)  #回退键
# sleep(2)
# el.send_keys("美女")
# sleep(2)
# el.send_keys(Keys.CONTROL,"a")
# sleep(2)
# el.send_keys(Keys.CONTROL,"c")
# sleep(2)
# el.send_keys(Keys.CONTROL,"v")

# 下拉框
#     通过select元素创建出Select对象，通过对象的方法选中选项
#     1、select_by_index()  根据option索引来定位，从0开始
#     2、select_by_value()  根据option属性value值来定位
#     3、select _by_visible_text()  根据option显示文本来定位
# select = Select(driver.find_element_by_id("adress"))
# select.select_by_index(0)
# select.select_by_value("sc")
# select.select_by_visible_text("四川")

# 页面滚动
# driver.maximize_window()
# # 设置页面滚动到的位置，尽量设置超过电脑屏幕的大小，这样会滚到最底下
# js_str = "window.scrollTo(0, 10000)"
# # 执行js代码
# driver.execute_script(js_str)

# 警告框
# alert = driver.switch_to.alert
# # 打印警告框的文本
# print(alert.text)
# # 点击取消
# alert.dismiss()
# # 点击确定
# alert.accept()

# sleep(2)
# driver.find_element_by_xpath("//*[@text()=‘下一页’]").click()

# frame切换
# # 切换到具体某个frame页面做操作
# driver.switch_to.frame("login_frame")
# sleep(2)
# driver.find_element_by_id("u").send_keys("11111111111")
# # 切换回原始的页面
# driver.switch_to.default_content()

# 页面切换
# driver.find_element_by_id("kw").send_keys("美女")
# driver.find_element_by_id("su").click()
#
# sleep(2)
# driver.find_element_by_xpath("//*[@id='1']/div/div[1]/div/div[1]/a[1]/img").click()
# # 切换页面，获取当前的handle值：先获取所有的handle，在通过传入的索引打开对应的页面，新打开的页面在所有handle列表的最后面
# # handle的获取：
#     # 1、driver.window_handles   获取所有的handle
#     # 2、driver.current_window_handle  获取当前页面的handle
#     # 3、driver.switch_to.window(handle)  切换窗口到对应页面
# driver.switch_to.window(driver.window_handles[1])
# sleep(2)
# driver.find_element_by_class_name("mediacy-upper").click()

# 截图
# driver.get_screenshot_as_file("beatifulgirl.png")

# cookies   存放用户的信息
# driver.add_cookie({"name":'BDUSS',"value":'gxTHc4bWVsR25XVzVYc0IwOEdCTG94RWVFNWVEU3ZiTVV3c3FSZldqWEpWS3hoRVFBQUFBJCQAAAAAAAAAAAEAAACMNurFv7S~tL-0yrLDtGhvbWUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMnHhGHJx4Rha0'})
# driver.add_cookie({"name":'BAIDUID',"value":'1108229BEEEC8E2DC5C008AD7C902429'})
# sleep(2)
# driver.refresh()

sleep(2)
driver.quit()