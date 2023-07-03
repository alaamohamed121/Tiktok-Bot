from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://www.tiktok.com/')


wait =input("skiP:")




def start():
        while True:  
            try:  
                repluy_button = driver.find_elements(By.XPATH, "//span[@data-e2e='comment-reply-1']")
                if repluy_button:
                    repluy_button[0].click()
                time.sleep(2)
                filename = "users.txt"

                with open(filename, "r") as file:
                    data = file.readlines()
                mention_button = driver.find_element(By.CSS_SELECTOR, ".tiktok-ii2xqx-DivMentionButton svg")
                comment_element = driver.find_element(By.XPATH, "//div[@class='notranslate public-DraftEditor-content']")
                for i in range(4):
                    if data:
                        if mention_button:
                            mention_button.click()
                        time.sleep(2)
                        if comment_element:
                            comment_element.send_keys(data.pop(0))
                        time.sleep(10)
                        form = driver.find_elements(By.XPATH ,"//span[@class='tiktok-evv4sm-SpanInfoNickname e16bf9xh9']")
                        if form:
                            form[0].click()
                        time.sleep(3)

                    if i == 3:
                        comment_element.send_keys("allah")
                        time.sleep(3)
                        post = driver.find_element(By.CSS_SELECTOR, ".tiktok-1ql4f2a-DivPostButton")
                        post.click()
                        time.sleep(8)
                with open(filename, "w") as file:
                    file.writelines(data)
                time.sleep(4)
            except:
                next

if wait == "1":
    start()






