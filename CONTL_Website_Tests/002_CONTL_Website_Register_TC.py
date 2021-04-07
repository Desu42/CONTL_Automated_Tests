import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


class TestContinentalWebsiteRegister:

    base_url = "https://alexandrularion.github.io/hotel-continental/"

    # It's good. Fields require a certain formatting.
    @allure.severity(allure.severity_level.CRITICAL)
    def test_register(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        btn_register = driver.find_element_by_xpath('//*[@id="header"]/div[1]/div[2]/div[2]/a[2]')
        btn_register.click()

        # I think username should be Full Name in website
        user_name = driver.find_element_by_id("username")
        user_name.send_keys("Cristina Moldovan")

        email = driver.find_element_by_id("email_reg")
        email.send_keys("cristina_m70@yahoo.com")

        password = driver.find_element_by_id("psw")
        password.send_keys("example_password")

        repeat_password = driver.find_element_by_id("psw-repeat")
        repeat_password.send_keys("example_password")

        phone_number = driver.find_element_by_id("about")
        phone_number.send_keys("0793354438")

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
