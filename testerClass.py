from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep, ctime

BANDCAMP_FIRSTPAGE='https://bandcamp.com/'

class BandCamp():
    def __init__(self):
        # Create a headless driver
        opts = Options()
        opts.add_argument("--disable-extensions")
        opts.add_argument("--headless")  
        self.driver = Firefox(options=opts,executable_path=r'My computers path')
        self.driver.get(BANDCAMP_FIRSTPAGE)

        # Track list related state
        self._current_track_number = 1
        self.track_list = []
        self.tracks()

    def tracks(self):
        '''
        Query the page to populate a list of available tracks.
        '''

        # Sleep to give the driver time to render and finish any animations
        sleep(2)

        # Get the container for the visible track list
        discover_section = self.driver.find_element_by_class_name('discover-results')
        left_x = discover_section.location['x']
        right_x = left_x + discover_section.size['width']

        # Filter the items in the list to include only those we can click
        discover_items = self.driver.find_elements_by_class_name('discover-item')
        self.track_list = [t for t in discover_items
                           if t.location['x'] >= left_x and t.location['x'] < right_x]

        # Print the available tracks to the screen
        for (i,track) in enumerate(self.track_list):
            print('[{}]'.format(i+1))
            lines = track.text.split('\n')
            print('Album  : {}'.format(lines[0]))
            print('Artist : {}'.format(lines[1]))
            if len(lines) > 2:
                print('Genre  : {}'.format(lines[2]))
        self.driver.close()
        self.driver.quit()          
    
if __name__ == '__main__':
    BandCamp()      