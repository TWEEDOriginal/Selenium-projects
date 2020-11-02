from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    opts = Options()
    opts.add_argument("--disable-extensions")
    opts.add_argument("--headless")
    driver = Firefox(options=opts,executable_path=r'My computers path')
    driver.get('https://bandcamp.com')
    print(driver.title)
    search_form = driver.find_element_by_class_name('you-autocomplete-me')
    search_form.send_keys('kendrick lamar')
    search_form.submit()
    try:
        page_content = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "result-items"))) 
        results = page_content.find_elements_by_class_name('searchresult') 
        for result in results:
            header = result.find_element_by_class_name('heading')
            print(header.text)
            
    except:
        driver.close()
        driver.quit()

    driver.close()
    driver.quit()  

if __name__ == '__main__':
    main()      