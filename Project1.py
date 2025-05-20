from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# pip install selenium==4.0.0.b4

s = Service("C:\prg\python-prg\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://www.instagram.com")
time.sleep(3)
# //*[@id="loginForm"]/div[1]/div[1]/div/label/input
# username = driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[1]/div/label/input""")
username = driver.find_element_by_xpath("""//*[@id="loginForm"]/div[1]/div[1]/div/label/input""")
username.send_keys("_ayoaxo_")
# //*[@id="loginForm"]/div[1]/div[2]/div/label/input
# password = driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[2]/div/label/input""")
password = driver.find_element_by_xpath("""//*[@id="loginForm"]/div[1]/div[2]/div/label/input""")
password.send_keys("_ayoaxo_pwd_")
password.send_keys(Keys.ENTER)
time.sleep(3)
# //*[@id="mount_0_0_sV"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[5]/div/div/span/div
# /html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[5]/div/div/span/div/a
# driver.find_element_by_xpath("""//*[@id="mount_0_0_sV"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[5]/div/div/span/div""")
driver.find_element_by_xpath("""/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[5]/div/div/span/div/a""").click()
time.sleep(3)
# "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[3]/button[1]"
driver.find_element_by_xpath("""/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[3]/button[1]""").click()
time.sleep(2)
# /html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div
driver.find_element_by_xpath("""/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div""").click()
time.sleep(1)
# /html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input
friend_username = driver.find_elment_by_xpath("""/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input""")
friend_username.send_keys("i_ayushijain_")
# friend_username.send_keys("wscubetechindia")
time.sleep(2)
# /html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div[1]/div[1]/div
driver.find_element_by_xpath("""/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div[1]/div[1]/div""").click()
time.sleep(4)
# /html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div
driver.find_element_by_xpath("""/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div""").click()
time.sleep(3)
# /html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]
for i in range(0,51):
    message = driver.find_elment_by_xpath("""/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]""")
    message.send_keys("mere paise wapis de")
    # message.send_keys("hello")
    message.send_keys(Keys.ENTER)
    time.sleep(0.5)