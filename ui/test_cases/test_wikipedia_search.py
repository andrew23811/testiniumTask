import time
import unittest
from selenium import webdriver
from pages import home_page


class BotManagementTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver.get_screenshot_as_file("screenshot.png")

    def test_search_valid_keyword(self):
        Homepages = home_page.HomePage(self.driver)
        Homepages.fill_search_bar("software testing")
        time.sleep(1)
        Homepages.click_search_button()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, "https://en.wikipedia.org/wiki/Software_testing")

    def test_search_invalid_keyword(self):
        Homepages = home_page.HomePage(self.driver)
        Homepages.fill_search_bar("kjashdkajshdkajsdkas")
        time.sleep(1)
        Homepages.click_search_button()
        time.sleep(2)
        assert "There were no results" in self.driver.page_source

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()
