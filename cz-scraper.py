from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import os


print("Write...")
Art = input("HTTP | SOCKS4 | SOCKS5 \n")

chop = webdriver.ChromeOptions()
chop.add_extension('extension_1_39_2_0.crx')
driver = webdriver.Chrome(chrome_options = chop)

f = open("Proxys.txt", "w")
f.close()


driver.get("http://free-proxy.cz/en/")

if Art == "HTTP":
    HTTP = driver.find_element_by_id("frmsearchFilter-protocol-1")
    HTTP.click()
elif Art == "SOCKS4":
    SOCKS4 = driver.find_element_by_id("frmsearchFilter-protocol-4")
    SOCKS4.click()
elif Art == "SOCKS5":
    SOCKS5 = driver.find_element_by_id("frmsearchFilter-protocol-5")
    SOCKS5.click()

suche = driver.find_element_by_id("frmsearchFilter-send")
suche.click()

i = 0
while i < 5:
    export = driver.find_element_by_id("clickexport")
    export.click()
    liste = driver.find_element_by_id("zkzk").text

    f = open("Proxys.txt", "a")
    f.write(liste)
    f.write("\n")

    if i <4:
        weiter = driver.find_element_by_link_text("Next »")
        weiter.click()
        time.sleep(1)

    i = i + 1

f.close()


time.sleep(1)
driver.quit()