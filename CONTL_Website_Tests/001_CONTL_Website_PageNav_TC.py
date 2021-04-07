import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
# from selenium.webdriver import ActionChains


# The images are huge. It takes a very long time to load the pages.
@allure.severity(allure.severity_level.NORMAL)
class TestContinentalHomePage:

    base_url = "https://alexandrularion.github.io/hotel-continental/"

    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)
        status = driver.find_element_by_class_name("logo").is_displayed()
        assert status
        driver.close()

    @allure.severity(allure.severity_level.BLOCKER)
    def test_load_home_page(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        assert "Continental" in driver.title
        driver.close()
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_home_page(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        home_page_button = driver.find_element_by_class_name("home")
        home_page_button.click()

        home_page_button_url = "https://alexandrularion.github.io/hotel-continental/index.html"

        if home_page_button_url == driver.current_url:
            driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Navigation_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False
    
    @allure.severity(allure.severity_level.BLOCKER)
    def test_rooms_page(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        rooms_page_button = driver.find_element_by_class_name("rooms")
        rooms_page_button.click()

        rooms_page_button_url = "https://alexandrularion.github.io/hotel-continental/rentroom.html"

        if rooms_page_button_url == driver.current_url:
            driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Navigation_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_services_page(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        services_page_button = driver.find_element_by_class_name("services")
        services_page_button.click()

        services_page_button_url = "https://alexandrularion.github.io/hotel-continental/services.html"

        if services_page_button_url == driver.current_url:
            driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Navigation_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False
    
    @allure.severity(allure.severity_level.NORMAL)
    def test_about_us_page(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        about_page_button = driver.find_element_by_class_name("about")
        about_page_button.click()

        about_page_button_url = "https://alexandrularion.github.io/hotel-continental/about.html"

        if about_page_button_url == driver.current_url:
            driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Navigation_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False
    
    @allure.severity(allure.severity_level.BLOCKER)
    def test_contact_page(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        contact_page_button = driver.find_element_by_class_name("contact")
        contact_page_button.click()

        contact_page_button_url = "https://alexandrularion.github.io/hotel-continental/contact.html"

        if contact_page_button_url == driver.current_url:
            driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Navigation_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False
    
    # Book now is the same page as rent room
    @allure.severity(allure.severity_level.BLOCKER)
    def test_book_now_page(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        book_page_button = driver.find_element_by_class_name("book_button")
        book_page_button.click()

        book_page_button_url = "https://alexandrularion.github.io/hotel-continental/rentroom.html"

        if book_page_button_url == driver.current_url:
            driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Navigation_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False
    
    # As of now, clicking on either Payment options or T&C takes you to the same page
    @allure.severity(allure.severity_level.CRITICAL)
    def test_information_page(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        payment_page_button = driver.find_element_by_class_name("options")
        payment_page_button.click()

        payment_page_button_url = "https://alexandrularion.github.io/hotel-continental/information.html"

        if payment_page_button_url == driver.current_url:
            driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Navigation_Test",
                          attachment_type=AttachmentType.PNG)
            driver.close()
            assert False
