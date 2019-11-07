from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://yf.a99.live/")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("18055779893")
