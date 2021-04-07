import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


@allure.severity(allure.severity_level.NORMAL)
class TestContinentalHomePage:

    base_url = "https://alexandrularion.github.io/hotel-continental/"

    @allure.severity(allure.severity_level.BLOCKER)
    def test_load_home_page(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        assert "Continental" in driver.title
        driver.close()

    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)
        status = driver.find_element_by_class_name("logo").is_displayed()
        assert status
        driver.close()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_in(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        btn_sign_in = driver.find_element_by_xpath("//*[@id='header']/div[1]/div[2]/div/a[3]")
        btn_sign_in.click()

        email = driver.find_element_by_id("email")
        email.send_keys("example@gmail.com")

        psw = driver.find_element_by_id("psw")
        psw.send_keys("example_password")

        sign_in = driver.find_element_by_class_name("registerbtn")
        sign_in.click()

        title = self.driver.title

        if title == "Welcome":
            driver.close()
            assert True

        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Login_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False
