from selenium.webdriver.common.by import By
from helpers.base_page import BasePage


class ResultsPage(BasePage):
    Title_field = (By.XPATH, 'class="mw-page-title-main"')
    No_result_field = (By.XPATH, '//*[@class="mw-search-nonefound"]')

    def get_title_field_value(self):
        self.find_element(self.Title_field)

    def get_No_result_field_value(self):
        self.find_element(self.No_result_field)
