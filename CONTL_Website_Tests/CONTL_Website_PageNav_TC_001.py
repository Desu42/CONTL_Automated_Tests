import pytest
import allure
# from time import sleep
from selenium import webdriver
# from selenium.common.exceptions import WebDriverException
# from webdriver_manager.chrome import ChromeDriverManager


class TestContinentalHomePage:

    base_url = "https://alexandrularion.github.io/hotel-continental/"

    def test_load_home_page(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        assert "Continental" in driver.title
        driver.close()

    def test_logo(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)
        status = driver.find_element_by_class_name("logo").is_displayed()
        assert status
        driver.close()

    def test_sign_in(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        btn_sign_in = driver.find_element_by_xpath("//*[@id='header']/div[1]/div[2]/div/a[3]")
        btn_sign_in.click()

        email = driver.find_element_by_id("email")
        email.send_keys('example@gmail.com')

        psw = driver.find_element_by_id("psw")
        psw.send_keys('example_password')

        sign_in = driver.find_element_by_class_name('registerbtn')
        sign_in.click()

        title = self.driver.title

        if title == "Welcome":
            driver.close()
            assert True

        else:
            driver.close()
            assert False


if __name__ == '__main__':
    pass
