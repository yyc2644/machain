#encoding utf-8
from selenium import webdriver

chromdriver = "/Users/yangyicheng/chromedriver"

driver = webdriver.Chrome("/Users/yangyicheng/chromedriver")
driver.get("http://www.baidu.com")