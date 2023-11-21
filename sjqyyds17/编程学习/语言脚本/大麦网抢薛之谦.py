import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 1. 修改为你的大麦网账号和密码
username = 'your_username'
password = 'your_password'

# 2. 初始化webdriver，这里使用Chrome浏览器
driver = webdriver.Chrome()

# 3. 登录大麦网
driver.get('https://www.damai.cn/')
login_button = driver.find_element_by_xpath('//*[@id="dm_login"]')
login_button.click()

# 等待登录页面加载
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))

# 输入用户名和密码
username_input = driver.find_element_by_xpath('//*[@id="username"]')
password_input = driver.find_element_by_xpath('//*[@id="password"]')
username_input.send_keys(username)
password_input.send_keys(password)

# 点击登录按钮
submit_button = driver.find_element_by_xpath('//*[@id="login"]/div[4]/div[1]')
submit_button.click()

# 4. 搜索薛之谦演唱会
search_input = driver.find_element_by_xpath('//*[@id="search-input"]')
search_input.send_keys('薛之谦')
search_input.send_keys(Keys.RETURN)

# 等待搜索结果加载
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="items"]')))

# 选择第一个搜索结果
first_result = driver.find_element_by_xpath('//div[@class="items"]/div[1]')
first_result.click()

# 5. 选择票价和数量
# 这里需要根据实际情况修改XPath，选择你想要的票价和数量
ticket_price = driver.find_element_by_xpath('//*[@id="ticket-price"]/div[2]')
ticket_price.click()
ticket_quantity = driver.find_element_by_xpath('//*[@id="ticket-quantity"]/div[2]')
ticket_quantity.click()

# 6. 点击“立即购买”按钮
buy_button = driver.find_element_by_xpath('//*[@id="buyBtn"]')
buy_button.click()

# 7. 确认订单（需要支付时手动操作）
# 请在这里添加确认订单和支付的逻辑，因为涉及到个人信息和付款，建议手动操作

# 8. 关闭浏览器
# driver.quit()