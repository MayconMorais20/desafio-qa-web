from behave import given, when, then
from selenium import webdriver
from pages.pratice_form_page import PraticeFormPage
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, random
fake = Faker('pt_BR') 

@given('I fill all the fields with random data')
def step_fill_fields_with_random_data(context):
    # Create a driver if not already in context
    if not hasattr(context, 'driver'):
        context.driver = webdriver.Chrome() 
        
    context.pratice_form_page = PraticeFormPage(context.driver)
    
    wait = WebDriverWait(context.pratice_form_page.driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, context.pratice_form_page.wait_load_element_page)))
    context.pratice_form_page.fill_first_name(fake.first_name())
    context.pratice_form_page.fill_last_name(fake.user_name())
    context.pratice_form_page.fill_email(fake.email())
    context.pratice_form_page.fill_gender()
    context.pratice_form_page.fill_mobile_number(''.join([str(random.randint(0, 9)) for _ in range(10)]))
    context.pratice_form_page.fill_date_of_birth()
    context.pratice_form_page.fill_subjects()
    context.pratice_form_page.select_hobbies("sports")
    context.pratice_form_page.select_file_to_picture()
    context.pratice_form_page.fill_current_address(fake.address())
    context.pratice_form_page.select_btn_state()
    context.pratice_form_page.select_btn_city()

@given('I submit the form')
def step_submit_form(context):
    context.pratice_form_page.click_btn_submit()
    time.sleep(1.5)

@when('I should see a pop-up message')
def step_verify_popup_message(context):
    context.pratice_form_page.validate_submit_popup_message()

@then('I close the pop-up')
def step_close_popup_message(context):
    context = PraticeFormPage(context.driver)
    context.close_popup_message()
    context.driver.quit()
