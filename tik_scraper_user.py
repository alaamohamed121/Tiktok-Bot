from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm"

driver = webdriver.Chrome()
driver.get(url)

time.sleep(2)
while True:
    skip = input("Enter any value to start scraping:")
    def start():
        links = driver.find_elements(By.XPATH,"//a[@class='e1g2efjf4 tiktok-1oblbwp-StyledLink-StyledUserLinkName er1vbsz0']")

        with open("users.txt", "a") as file:
            for link in links:
                href = link.get_attribute("href")
                cleaned_href = href.replace("https://www.tiktok.com/@", "")
                file.write(cleaned_href + "\n")

        def remove_duplicates_from_file(file_path):
            unique_lines = set()
            with open(file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line not in unique_lines:
                        unique_lines.add(line)
            with open(file_path, "w") as file:
                for line in unique_lines:
                    file.write(line + "\n")

        file_path = "users.txt"

        remove_duplicates_from_file(file_path)

    start()
