from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
import time, os

class PraticeFormPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait_load_element_page = '//input[@placeholder="First Name"]'
        self.__first_name_locator = '//input[@placeholder="First Name"]'
        self.__last_name_locator = '//input[@placeholder="Last Name"]'
        self.__email_locator = '//input[@placeholder="name@example.com"]'
        self.__gender_locator = '//label[@for="gender-radio-2"]'
        self.__mobile_number_locator = '//input[@id="userNumber"]'
        self.__btn_date_of_birth_locator = '//input[@id="dateOfBirthInput"]'
        self.__subjects_locator = '//input[@id="subjectsInput"]'
        self.__hobbies_sports_locator = '//label[@for="hobbies-checkbox-1"]'
        self.__hobbies_reading_locator = '//label[@for="hobbies-checkbox-2"]'
        self.__hobbies_music_locator = '//label[@for="hobbies-checkbox-3"]'  
        self.__btn_select_file_picture_locator = '//input[@id="uploadPicture"]' 
        self.__current_address_locator = '//textarea[@id="currentAddress"]'
        self.__btn_statelocator = '//div[@id="state"]'
        self.__value_state_locator = '//div[@id="stateCity-wrapper"]//div[contains(text(), "NCR")]'
        self.__btn_city_locator = '//div[@id="city"]'
        self.__value_city_locator = '//div[@id="stateCity-wrapper"]//div[contains(text(), "Delhi")]'
        self.__btn_submit_locator = '//button[@id="submit"]'       
        self.__submit_confirm_popup_message_locator = '//*[text() = "Thanks for submitting the form"]'
        self.__close_popup_button_locator = '//button[@id="closeLargeModal"]'

    def fill_first_name(self, first_name):
        self.driver.find_element("xpath", self.__first_name_locator).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element("xpath", self.__last_name_locator).send_keys(last_name)

    def fill_email(self, email):
        self.driver.find_element("xpath", self.__email_locator).send_keys(email)

    def fill_gender(self):
        self.driver.find_element("xpath", self.__gender_locator).click()

    def fill_mobile_number(self, mobile_number):
        self.driver.find_element("xpath", self.__mobile_number_locator).send_keys(mobile_number)

    def fill_date_of_birth(self):
        self.driver.find_element("xpath", self.__btn_date_of_birth_locator).send_keys("\ue009\ue003\ue009\ue003\ue009\ue003\ue009\ue003\ue009")
        time.sleep(1)
        self.driver.find_element("xpath", self.__btn_date_of_birth_locator).send_keys("\ue009" + " 18 Apr 2007")
        self.driver.find_element("xpath", self.__btn_date_of_birth_locator).send_keys("18 Apr 2007\ue007")
        time.sleep(1)

    def fill_subjects(self):
        time.sleep(0.5)
        subjects_input = self.driver.find_element("xpath", self.__subjects_locator)
        subjects_input.send_keys("english")
        subjects_input.send_keys("\ue007")

    def select_hobbies(self, hobbiesType):
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        if hobbiesType.lower() == "sports":
            self.driver.find_element("xpath", self.__hobbies_sports_locator).click()
        elif hobbiesType.lower() == "reading":
            self.driver.find_element("xpath", self.__hobbies_reading_locator).click()
        elif hobbiesType.lower() == "music":
            self.driver.find_element("xpath", self.__hobbies_music_locator).click()
        else:
            raise Exception("Invalid hobbies type")
        
    def select_file_to_picture(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        txt_path = os.path.join(project_root, "data", "file_to_picture.txt")

        # Send the file path directly to the input element
        file_input = self.driver.find_element("xpath", self.__btn_select_file_picture_locator)
        file_input.send_keys(txt_path)

    def fill_current_address(self, address):
        self.driver.find_element("xpath", self.__current_address_locator).send_keys(address)

    def select_btn_state(self):
        self.driver.find_element("xpath", self.__btn_statelocator).click()
        time.sleep(1)
        self.driver.find_element("xpath", self.__value_state_locator).click()

    def select_btn_city(self):
        time.sleep(0.5)
        self.driver.find_element("xpath", self.__btn_city_locator).click()
        time.sleep(1)
        self.driver.find_element("xpath", self.__value_city_locator).click()

    def click_btn_submit(self):
        self.driver.find_element("xpath", self.__btn_submit_locator).click()

    def validate_submit_popup_message(self):
        wait = WebDriverWait(self.driver, 10)
        popup = wait.until(EC.visibility_of_element_located((By.XPATH, self.__submit_confirm_popup_message_locator)))

        assert popup.is_displayed(), "Submit confirmation popup is not displayed after 10 seconds wait"
    
    def close_popup_message(self):
        self.driver.find_element("xpath", self.__close_popup_button_locator).click()     