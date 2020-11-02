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
    tracks = driver.find_elements_by_class_name('discover-item')
    print(len(tracks))
    tracks[5].click()
    time.sleep(120)
    driver.close() 
    driver.quit()  

if __name__ == '__main__':
    main()      