from selenium import webdriver
driver=webdriver.Firefox() #启动火狐浏览器实例
driver.get("http://dev.zjgt168.com")   #访问zjgt
driver.get_cookies()