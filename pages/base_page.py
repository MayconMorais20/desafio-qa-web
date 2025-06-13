class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def get_text(self, by, value):
        element = self.find_element(by, value)
        return element.text

    def is_element_present(self, by, value):
        try:
            self.find_element(by, value)
            return True
        except:
            return False