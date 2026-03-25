class BasePage:
        
        def __init__(self, driver):
            self.driver = driver

        def do_click(self, locator):
            self.driver.find_element(locator).click()

        def do_send_keys(self, locator, value):
            self.driver.find_element(locator).send_keys(value)

        def get_title(self):
            return self.driver.title

        def get_element(self, locator):
            return self.driver.find_element(locator)