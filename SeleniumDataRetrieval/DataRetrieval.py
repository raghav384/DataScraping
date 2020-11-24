from selenium import webdriver
chromedriver_location = "C:/Users/Dell/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)
driver.get("https://pharmeasy.in/")
searchbar_xpath = '//*[@id="content"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/input'
searchbutton_xpath = '//*[@id="content"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]'
searchbar_element = driver.find_element_by_xpath(searchbar_xpath)
searchbar_element.send_keys("crocin")
searchbutton_element = driver.find_element_by_xpath(searchbutton_xpath)
searchbutton_element.click()

