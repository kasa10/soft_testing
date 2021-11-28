from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import sys
import parse

import os
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)

use_step_matcher("re")


@given("The PHPTravels sign up page is open")
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.phptravels.net/signup")
    context.driver.maximize_window()
    WebDriverWait(context.driver, 10) #aaaa
    assert context.driver.title == "Signup - PHPTRAVELS"


@given("Verify registration page")
def step_impl(context):
    assert context.driver.title == "Signup - PHPTRAVELS"


@when('The user record has a first name of "(?P<fname>.+)"')
def step_impl(context, fname):
    context.driver.find_element(By.NAME, "first_name").send_keys(fname)


@step('the user record has a last name of "(?P<lname>.+)"')
def step_impl(context, lname):
    context.driver.find_element(By.NAME, "last_name").send_keys(lname)


@step('Mobile Phone is "(?P<phone>.+)"')
def step_impl(context, phone):
    context.driver.find_element(By.NAME, "phone").send_keys(phone)


@step('Enter email "(?P<email>.+)"')
def step_impl(context, email):
    context.driver.find_element(By.NAME, "email").send_keys(email)




@step('Password of "(?P<password>.+)"')
def step_impl(context, password):
    context.driver.find_element(By.NAME, "password").send_keys(password)


@step("Signup button click")
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 500)")
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".btn-lg").click()


@then("The user must successfully create an account")
def step_impl(context):
    sleep(1)
    assert context.driver.find_element(By.CSS_SELECTOR, ".signup").is_displayed() #message about succes reg
    assert context.driver.title == "Login - PHPTRAVELS"


@then("The user get message that user already exist")
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert-danger").is_displayed() #user already exist message