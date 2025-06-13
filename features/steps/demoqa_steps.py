from behave import given
from selenium import webdriver
from pages.demoqa_page import DemoQAPage
from selenium.webdriver.common.by import By
from utils.config import Config
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@given('I open the DemoQA website')
def step_open_demoqa_website(context):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.get(Config.get_base_url())
    context.driver.maximize_window()
    context.demoqa_page = DemoQAPage(context.driver)
    

@given('I click on the Form')
def step_verify_forms_text(context):
    context.driver.find_element(By.XPATH, context.demoqa_page.forms_text_locator).click()
    context.driver.find_element(By.XPATH, context.demoqa_page.btn_pratice_forms_locator).click()