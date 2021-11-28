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
import pyautogui

import os
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)

use_step_matcher("re")


@step("The Contact us link is clicked")
def step_impl(context):
    sleep(2)
    context.driver.execute_script("window.scrollTo(0, 5800)")
    sleep(5)
    context.driver.find_element_by_xpath("/html/body/section[10]/div[1]/div[1]/div[1]/div/ul/li[3]/a").click()
    sleep(3)



@given("Verify that contact page is opened")
def step_impl(context):
    assert context.driver.title == "Contact - PHPTRAVELS"


@when('The user enter name "(?P<name>.+)"')
def step_impl(context, name):
    context.driver.find_element(By.NAME, "name").send_keys(name)


@step('The user enter email "(?P<email>.+)"')
def step_impl(context, email):
    if email == "N/A":
        context.driver.find_element(By.NAME, "email").send_keys("")
    else:
        context.driver.find_element(By.NAME, "email").send_keys(email)


@step('The user enter message "(?P<message>.+)"')
def step_impl(context, message):
    context.driver.find_element(By.NAME, "message").send_keys(message)



@step("Send button click")
def step_impl(context):
    button1 = context.driver.find_element_by_xpath("// *[ @ id = 'button']")
    sleep(1)
    context.driver.execute_script("arguments[0].removeAttribute('disabled')", button1)
    sleep(1)
    context.driver.execute_script("window.scrollTo(0, 100)")
    sleep(3)
    button1.click()
    sleep(1)


@then("Get error message")
def step_impl(context):
    error = context.driver.find_element_by_xpath("/html/body").text
    if "Invalid address" in error:
        print(error)
        assert len(error)>0
    else:
        element = context.driver.find_element(By.NAME, "email")
        x = element.get_attribute("validationMessage")
        sleep(1)
        assert len(x)>0
        print(x)




@then("Message sent successfully")
def step_impl(context):
    text = context.driver.find_element_by_xpath("/ html / body / section[2] "
                                                "/ div / div / div[1] / div / div[2] / div[1]").text
    print(text)
    assert 'Message sent successfully' in text