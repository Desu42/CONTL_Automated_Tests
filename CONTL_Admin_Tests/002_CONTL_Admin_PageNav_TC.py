import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


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
