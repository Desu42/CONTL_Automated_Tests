import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@allure.severity(allure.severity_level.NORMAL)
class TestContinentalAdminAddEmployee:

    base_url = "https://continental.netlify.app/index.html#"

    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_employee(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        employees_panel = driver.find_element_by_xpath("/html/body/div[3]/div[2]/ul/li[2]/a")
        employees_panel.click()

        add_employee_btn = driver.find_element_by_class_name("addEmployeeBtn")
        add_employee_btn.click()

        name = driver.find_element_by_id("names")
        name.send_keys("Florin Balan")

        position = Select(driver.find_element_by_id('position'))
        position.select_by_visible_text('Accountant')

        phone = driver.find_element_by_id("phone")
        phone.send_keys("0762981128")

        email = driver.find_element_by_id("emails")
        email.send_keys("florin.balan@yahoo.com")

        pswd = driver.find_element_by_id("passwords")
        pswd.send_keys("9PpN7=tt")

        btn_add = driver.find_element_by_xpath("//*[@id='modal_content2']/div[6]/button[2]")
        btn_add.click()

        driver.close()

        # TO DO
        # How to check if it will be displayed? See when API implemented.

        """
            driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Navigation_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False
        """
