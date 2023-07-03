from selenium import webdriver
import time
from selenium.webdriver.common.by import By

urlv = input("enter url:")
chooes = input("enter num:")
def views():
    # Create a new instance of the chrome driver
    driver = webdriver.Chrome()

    # Navigate to the URL
    url = "https://zefoy.com/"
    driver.get(url)

    time.sleep(30)

    view_box = driver.find_element(By.XPATH, "//button[@class='btn btn-primary rounded-0 menu4']")

    view_box.click()
    time.sleep(3)

    url_input = driver.find_elements(By.XPATH, "//input[@class='form-control text-center font-weight-bold rounded-0']")
    if url_input:
        url_input[3].send_keys(urlv)


    time.sleep(2)
    search = driver.find_elements(By.CSS_SELECTOR, ".input-group-append .btn, .input-group-prepend .btn")
    if search:

        search[3].click()


    time.sleep(10)

    submit_button = driver.find_elements(By.XPATH,"//form[@action='c2VuZC9mb2xeb3dlcnNfdGlrdG9V']")
    if submit_button:
        submit_button[1].click()

    time.sleep(180)
    while True:

        search[3].click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//form[@onsubmit='comviews()']").click()

        time.sleep(180)



def share():
    # Create a new instance of the chrome driver
    driver = webdriver.Chrome()

    # Navigate to the URL
    url = "https://zefoy.com/"
    driver.get(url)

    time.sleep(30)

    view_box = driver.find_element(By.XPATH, "//button[@class='btn btn-primary rounded-0 menu7']")

    view_box.click()
    time.sleep(3)

    url_input = driver.find_elements(By.XPATH, "//input[@class='form-control text-center font-weight-bold rounded-0']")
    if url_input:
        url_input[4].send_keys(urlv)


    time.sleep(2)
    search = driver.find_elements(By.CSS_SELECTOR, ".input-group-append .btn, .input-group-prepend .btn")
    if search:

        search[4].click()


    time.sleep(10)

    submit_button = driver.find_elements(By.XPATH,"//form[@action='c2VuZC9mb2xsb3dlcnNfdGlrdG9s']")
    if submit_button:
        submit_button[1].click()

    time.sleep(180)
    while True:

        search[4].click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//form[@onsubmit='comthearts()']").click()

        time.sleep(180)


def fav():
    # Create a new instance of the chrome driver
    driver = webdriver.Chrome()

    # Navigate to the URL
    url = "https://zefoy.com/"
    driver.get(url)

    time.sleep(30)

    view_box = driver.find_element(By.XPATH, "//button[@class='btn btn-primary rounded-0 menu8']")

    view_box.click()
    time.sleep(3)

    url_input = driver.find_elements(By.XPATH, "//input[@class='form-control text-center font-weight-bold rounded-0']")
    if url_input:
        url_input[5].send_keys(urlv)


    time.sleep(2)
    search = driver.find_elements(By.CSS_SELECTOR, ".input-group-append .btn, .input-group-prepend .btn")
    if search:

        search[5].click()


    time.sleep(10)

    submit_button = driver.find_elements(By.XPATH,"//form[@action='c2VuZF9mb2xsb3dlcnNfdGlrdG9L']")
    if submit_button:
        submit_button[1].click()

    time.sleep(180)
    while True:

        search[5].click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//form[@onsubmit='favhides()']").click()

        time.sleep(180)

if chooes == "1":
    views()
elif chooes == "2":
    share()
elif chooes == "3":
    fav()





