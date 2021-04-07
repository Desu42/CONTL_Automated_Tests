import allure
# from allure_commons.types import AttachmentType
# from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


@allure.severity(allure.severity_level.NORMAL)
class TestContinentalAdminAddRoom:

    base_url = "https://continental.netlify.app/index.html#"

    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_room(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        rooms_panel = driver.find_element_by_xpath("/html/body/div[3]/div[2]/ul/li[3]/a")
        rooms_panel.click()

        add_room_btn = driver.find_element_by_class_name("addRoomBtn")
        driver.implicitly_wait(3)
        ActionChains(driver).move_to_element(add_room_btn).click(add_room_btn).perform()

        name = driver.find_element_by_id('namer')
        name.send_keys("Room 0.1")

        room_type = Select(driver.find_element_by_id('type'))
        room_type.select_by_visible_text('Suite')

        price_per_night = driver.find_element_by_id("price-night")
        price_per_night.send_keys("200")

        room_status = Select(driver.find_element_by_id("status"))
        room_status.select_by_visible_text('Cleaning in progress')
        # price_per_night.send_keys(Keys.ENTER)

        add_btn = driver.find_element_by_id("modal_content3")
        add_btn.click()

        driver.close()
