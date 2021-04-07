import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
# from time import sleep


# 001 TC
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


# 002 TC
@allure.severity(allure.severity_level.NORMAL)
class TestContinentalAdminNavigation:

    base_url = "https://continental.netlify.app/index.html#"

    @allure.severity(allure.severity_level.BLOCKER)
    def test_navigate_employees(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        employees_panel = driver.find_element_by_xpath("/html/body/div[3]/div[2]/ul/li[2]/a")
        employees_panel.click()
        employees_url = "https://continental.netlify.app/employees.html"

        if employees_url == driver.current_url:
            driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Navigation_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_navigate_rooms(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        rooms_panel = driver.find_element_by_xpath("/html/body/div[3]/div[2]/ul/li[3]/a")
        rooms_panel.click()
        rooms_url = "https://continental.netlify.app/rooms.html"

        if rooms_url == driver.current_url:
            driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Navigation_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_navigate_reservations(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        reservations_panel = driver.find_element_by_xpath("/html/body/div[3]/div[2]/ul/li[4]/a")
        reservations_panel.click()
        reservations_url = "https://continental.netlify.app/reservations.html"

        if reservations_url == driver.current_url:
            driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Navigation_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_navigate_emails(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        emails_panel = driver.find_element_by_xpath("/html/body/div[3]/div[2]/ul/li[5]/a")
        emails_panel.click()
        emails_url = "https://continental.netlify.app/emails.html"

        if emails_url == driver.current_url:
            driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Navigation_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False

    @allure.severity(allure.severity_level.BLOCKER)
    def test_navigate_dashboard(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)

        login = driver.find_element_by_xpath("/html/body/form/input[3]")
        login.click()

        dashboard_panel = driver.find_element_by_xpath("/html/body/div[3]/div[2]/ul/li[1]/a")
        dashboard_panel.click()
        dashboard_url = "https://continental.netlify.app/dashboard.html"

        if dashboard_url == driver.current_url:
            driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Navigation_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False


# 003 TC
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
        driver.implicitly_wait(3)
        ActionChains(driver).move_to_element(add_employee_btn).click(add_employee_btn).perform()

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


# 004 TC
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


# 005 TC
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


# 006 TC
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


# 007 TC
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
