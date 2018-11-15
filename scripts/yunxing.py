from base.base_driver import init_driver
from page.page import Page


class YunXing():
    def setup(self):

        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def YunXing(self):

        self.page.search.first_click()
        self.page.search.first_click_search('hello')
        self.page.seeting.second_click_search()
