from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
import time

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
            wd = self.wd
            wd.get("http://localhost/addressbook/")
            #time.sleep(2)


    def destroy(self):
        self.wd.quit()