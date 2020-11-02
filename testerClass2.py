from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep, ctime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BANDCAMP_FIRSTPAGE='https://bandcamp.com/'

class BandCamp():
    def __init__(self):
        # Create a headless driver
        opts = Options()
        opts.add_argument("--disable-extensions")
        opts.add_argument("--headless")  
        self.driver = Firefox(options=opts,executable_path=r'My computers path')
        self.driver.get(BANDCAMP_FIRSTPAGE)

       
        self.article_list = []
        self.articles()

    def articles(self):
        window_before = self.driver.window_handles[0]
        print(len(self.driver.window_handles))
        sleep(1)
        section = self.driver.find_elements_by_class_name('section-title')
        for i in section:
             if (i.text.lower().find('bandcamp daily') > -1):
                    i.text.click()

        '''try:
            page_content = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "p-daily-home"))
            self.article_list = self.driver.find_elements_by_class_name('list-article')

            
            for (i,article) in enumerate(self.article_list):
                print('[{}]'.format(i+1))
                print(article.text)
            print(self.article_list)      
            )'''
        sleep(10)
        #window_after = self.driver.window_handles[1]
        #driver.switch_to.window(window_after)
        print(len(self.driver.window_handles))
        print(self.driver.title)
        #page_content = self.driver.find_element_by_id("p-daily-home")    
        #print(page_content.text)
            
       
        print('tweed')
        self.driver.quit()  
                
    

    
if __name__ == '__main__':
    BandCamp()      