import allure
# from allure_commons.types import AttachmentType
# from selenium.webdriver.common.keys import Keys
# from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


@allure.severity(allure.severity_level.NORMAL)
class TestContinentalAdminEditRoom:

    base_url = "https://continental.netlify.app/index.html#"

    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_room(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        rooms_panel = driver.find_element_by_xpath("/html/body/div[3]/div[2]/ul/li[3]/a")
        rooms_panel.click()

        edit_room_btn = driver.find_element_by_class_name("editRoomBtn")
        driver.implicitly_wait(3)
        ActionChains(driver).move_to_element(edit_room_btn).click(edit_room_btn).perform()

        name = driver.find_element_by_id('namer')
        name.send_keys("Room 0.4")

        room_type = Select(driver.find_element_by_id('type'))
        room_type.select_by_visible_text('Double')

        price_per_night = driver.find_element_by_id("price-night")
        price_per_night.send_keys("40")

        room_status = Select(driver.find_element_by_id("status"))
        room_status.select_by_visible_text('Occupied')
        # price_per_night.send_keys(Keys.ENTER)

        update_btn = driver.find_element_by_id("edit_room_form")
        update_btn.click()

        driver.close()
