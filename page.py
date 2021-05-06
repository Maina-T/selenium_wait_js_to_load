from selenium import webdriver
from selenium.webdriver.chrome.options import Options # to set a headless browser
from shutil import which # to look for driver location
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Page:

    def get_page(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("chromedriver")

        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        driver.set_window_size(1920,1080) # to set window size inorder to get all elements
        driver.get("https://www.jumia.co.ke/")

        # wait for the presence of js content and get the page source
        try:
            claim_btn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="sub"]'))
            )
            html = driver.page_source
            print(html)
        except Exception as e:
            print("Timeout happened no page load")
        
        driver.close()

if __name__ == '__main__':
    p = Page()
    p.get_page()