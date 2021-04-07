import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


@allure.severity(allure.severity_level.NORMAL)
class TestContinentalAdminLogin:

    base_url = "https://continental.netlify.app/index.html#"

    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_in_random_credentials(self):
        """BIG PROBLEM IF THIS PASSES"""
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        email_example = '@abcdefgh'
        password_example = '12345678'

        email_field = driver.find_element_by_xpath("/html/body/form/input[1]")
        email_field.send_keys(email_example)

        password_field = driver.find_element_by_xpath("/html/body/form/input[2]")
        password_field.send_keys(password_example)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        title = self.driver.title

        if title == "Contintental - Admin Panel":
            allure.attach(self.driver.get_screenshot_as_png(), name="Login_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert True
        else:
            driver.close()
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_in_no_credentials(self):
        """BIG PROBLEM IF THIS PASSES"""
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        title = self.driver.title

        if title == "Contintental - Admin Panel":
            allure.attach(self.driver.get_screenshot_as_png(), name="Login_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert True
        else:
            driver.close()
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_in_bad_credentials(self):
        """BIG PROBLEM IF THIS PASSES"""
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        email_example = 'logocah188@tlhao86.com'
        password_example = 'lOy9CaYkjh'

        email_field = driver.find_element_by_xpath("/html/body/form/input[1]")
        email_field.send_keys(email_example)

        password_field = driver.find_element_by_xpath("/html/body/form/input[2]")
        password_field.send_keys(password_example)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        title = self.driver.title

        if "Contintental - Admin Panel" in title:
            allure.attach(self.driver.get_screenshot_as_png(), name="Login_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert True
        else:
            driver.close()
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_sign_in_good_credentials(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        email_example = 'alexandru.damian3@student.usv.ro'
        password_example = 'lOy9CaYkjh'

        email_field = driver.find_element_by_xpath("/html/body/form/input[1]")
        email_field.send_keys(email_example)

        password_field = driver.find_element_by_xpath("/html/body/form/input[2]")
        password_field.send_keys(password_example)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        title = self.driver.title

        if "Contintental - Admin Panel" in title:
            driver.close()
            assert True

        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Login_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False
