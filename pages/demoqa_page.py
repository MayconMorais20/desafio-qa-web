class DemoQAPage:
    def __init__(self, driver):
        self.driver = driver
        self.forms_text_locator = "//h5[text()='Forms']"
        self.btn_pratice_forms_locator = '//span[@class="text" and text() ="Practice Form"]'

    def open_demoqa(self):
        self.driver.get("https://demoqa.com/")

    def is_forms_text_present(self):
        try:
            return self.driver.find_element("xpath", self.forms_text_locator).is_displayed()
        except:
            return False