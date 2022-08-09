from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"D:\_Selenium\chromedriver_win32\chromedriver.exe")
driver.get(r"https://in.bookmyshow.com/")
driver.maximize_window()
sleep(3)

driver.find_element_by_xpath("//span[text()='Bengaluru']").click()
sleep(3)

driver.find_element_by_xpath("//div[text()='Sign in']").click()
sleep(3)

driver.find_element_by_xpath("//input[@id='mobileNo']").send_keys(1234567890)
sleep(3)

driver.find_element_by_xpath("//button[@class='sc-hORach dSbYDX']").click()
sleep(3)

driver.find_element_by_xpath("//input[@class='sc-dymIpo cRKvaf']").send_keys(123456)
sleep(5)
driver.quit()
