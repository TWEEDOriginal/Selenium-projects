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
    x = driver.find_elements_by_class_name('item-page')
    print(len(x))
    for next_button in x:
      if (next_button.text.lower().find('next') > -1):
         next_button.click()
    time.sleep(5)

    discover_section = driver.find_element_by_class_name('discover-results')
    left_x = discover_section.location['x']
    right_x = left_x + discover_section.size['width']
    print(left_x)
    print(right_x)
    tracks = driver.find_elements_by_class_name('discover-item')
    trackee = [t for t in tracks
              if t.location['x'] >= left_x and t.location['x'] < right_x]
    assert len(trackee) == 8 
    print(len(trackee))    
    trackee[5].click()
    time.sleep(5)
    driver.quit()  

if __name__ == '__main__':
    main()      