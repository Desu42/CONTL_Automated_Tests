import allure
# from allure_commons.types import AttachmentType
# from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


@allure.severity(allure.severity_level.NORMAL)
class TestContinentalAdminEditEmployee:

    base_url = "https://continental.netlify.app/index.html#"

    @allure.severity(allure.severity_level.NORMAL)
    def test_add_employee(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        employees_panel = driver.find_element_by_xpath("/html/body/div[3]/div[2]/ul/li[2]/a")
        employees_panel.click()

        edit_btn = driver.find_element_by_class_name("editEmployeeBtn")
        driver.implicitly_wait(3)
        ActionChains(driver).move_to_element(edit_btn).click(edit_btn).perform()

        name = driver.find_element_by_id("names")
        name.clear()
        name.send_keys("Florin Balan")

        position = Select(driver.find_element_by_id('position'))
        position.select_by_visible_text('Accountant')

        phone = driver.find_element_by_id("phone")
        phone.clear()
        phone.send_keys("0762981128")

        email = driver.find_element_by_id("emails")
        email.clear()
        email.send_keys("florin.balan@yahoo.com")

        pswd = driver.find_element_by_id("passwords")
        pswd.clear()
        pswd.send_keys("9PpN7=tt")

        btn_update = driver.find_element_by_id("edit_employee_form")
        btn_update.click()

        driver.close()

        # TO DO
        # How to check if it will be displayed? See when API implemented.
