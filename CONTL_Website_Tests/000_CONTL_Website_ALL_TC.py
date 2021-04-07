import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
# from selenium.webdriver import ActionChains


# The images are huge. It takes a very long time to load the pages.
# 001 TC
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


# 002 TC
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


# 003 TC
class TestContinentalWebsiteLogin:

    base_url = "https://alexandrularion.github.io/hotel-continental/"

    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_in(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.maximize_window()
        driver.get(self.base_url)

        btn_sign_in = driver.find_element_by_xpath("//*[@id='header']/div[1]/div[2]/div/a[3]")
        btn_sign_in.click()

        email = driver.find_element_by_id("email")
        email.send_keys("example@gmail.com")

        psw = driver.find_element_by_id("psw")
        psw.send_keys("example_password")

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
