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

@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text


@given("The PHPTravels site is open")
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get("https://phptravels.com/demo")
    context.driver.maximize_window()
    WebDriverWait(context.driver, 10) #aaaa
    assert context.driver.title == "Demo Script Test drive - PHPTRAVELS"


@step("The Login link is clicked")
def step_impl(context):
    sleep(2)
    assert context.driver.find_element_by_xpath("//*[@id='Main']/section[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/a").is_displayed()
    context.driver.find_element_by_xpath('//*[@id="Main"]/section[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/a').click()
    sleep(10)
    context.driver.switch_to.window(context.driver.window_handles[1]) #page 2
    assert context.driver.title == "Login - PHPTRAVELS"




@given('Enter email "asdfghjkl@mail\.ru" and password "123"')
def enter_info(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input").send_keys("asdfghjkl@mail.ru")
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input").send_keys("123")



@when("Login button is clicked")
def step_impl(context):
    sleep(1)
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[3]/button").click()







@then("The error message is shown")
def step_impl(context):
    sleep(0.3)
    assert context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]").is_displayed()




@given('Enter email "" and password "123"')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input").send_keys(
        "")
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input").send_keys(
        "123")



@given('Enter email "example123" and password "12345"')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input").send_keys(
        "example123")
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input").send_keys(
        "12345")


@given('Enter email "asdf@mail.ru" and password ""')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input").send_keys(
        "asdf@mail.ru")
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input").send_keys(
        "")


@given('Enter email "" and password ""')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input").send_keys(
        "")
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input").send_keys(
        "")




@then("Text field error is shown")
def step_impl(context):


    element = context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input")
    sleep(2)
    x = element.get_attribute("validationMessage")
    sleep(1)
    if len(x)==0:
        element = context.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input")
        x = element.get_attribute("validationMessage")

    assert len(x)>0
    print(x)


@then("Page of user's account is opened")
def step_impl(context):
    assert context.driver.title == "Dashboard - PHPTRAVELS" #user's account page