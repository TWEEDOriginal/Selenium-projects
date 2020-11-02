from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
def main():
    opts = Options()
    opts.add_argument("--disable-extensions")
    opts.add_argument("--headless")
    #assert opts.headless
    driver = Firefox(options=opts,executable_path=r'My computers path')
    driver.get('https://bandcamp.com')
    #driver.find_element_by_class_name('playbutton').click()
    #tracks = driver.find_elements_by_class_name('discover-item')
    #print(len(tracks))
    #tracks[3].click()
    x = driver.find_elements_by_class_name('item-page')
    print(len(x))
    next_button = [e for e in x if e.text.lower().find('next') > -1]
    next_button.click()
    print(driver.title)
    driver.close()
    driver.quit()  
if __name__ == '__main__':
    main()  