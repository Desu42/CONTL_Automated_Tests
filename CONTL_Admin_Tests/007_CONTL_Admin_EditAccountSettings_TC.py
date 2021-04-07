import allure
# from allure_commons.types import AttachmentType
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver import ActionChains


@allure.severity(allure.severity_level.NORMAL)
class TestContinentalAdminEditAccountSettings:

    base_url = "https://continental.netlify.app/index.html#"

    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_room(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        settings = driver.find_element_by_class_name("settings")
        ActionChains(driver).move_to_element(settings).click(settings).perform()

        full_name = driver.find_element_by_id("name")
        full_name.clear()
        full_name.send_keys("Robert Soroceanu")

        email = driver.find_element_by_id("email")
        email.clear()
        email.send_keys("robert_soroceanu98@gmail.com")

        phone_number = driver.find_element_by_id("phone1")
        phone_number.clear()
        phone_number.send_keys("0730456652")

        password = driver.find_element_by_id("password1")
        password.send_keys("current_password")

        new_password = driver.find_element_by_id("password2")
        new_password.send_keys("@new_password1234")

        repeat_new_password = driver.find_element_by_id("password3")
        repeat_new_password.send_keys("@new_password1234")

        # for the moment, it works to send new_password and repeat_new_password as being different
        update_btn = driver.find_element_by_id("modal_content")
        update_btn.click()

        driver.close()
