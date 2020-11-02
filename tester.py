from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

def main():
    opts = Options()
    opts.add_argument("--disable-extensions")
    opts.add_argument("--headless")
    driver = Firefox(options=opts,executable_path=r'My computers path')
    driver.get('https://bandcamp.com')
    print(driver.title)
    driver.find_element_by_class_name('playbutton').click()
    time.sleep(500)
    driver.close()
    driver.quit()  

if __name__ == '__main__':
    main()      