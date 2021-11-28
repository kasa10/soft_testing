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
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(dir_path)

use_step_matcher("re")



@given("Subscribe field is displayed")
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 4008)")
    sleep(1)
    assert context.driver.find_element(By.ID, "exampleInputEmail1").is_displayed()
    sleep(1)



@when('Enter "(?P<email>.+)"')
def step_impl(context, email):
    sleep(1)
    context.driver.find_element(By.ID, "exampleInputEmail1").click()
    sleep(0.5)
    if email!="N/A":
        context.driver.find_element(By.ID, "exampleInputEmail1").send_keys(email)
    else:
        context.driver.find_element(By.ID, "exampleInputEmail1").send_keys("")


@step("Click Subscribe button")
def step_impl(context):
    context.driver.find_element(By.ID, "email_subscribe").click()


@then('Get error "(?P<message>.+)"')
def step_impl(context, message):
    sleep(1.5)
    text = context.driver.find_element_by_xpath("/ html / body / section[9] / div / div / div[2] "
                                         "/div / div / div / div / span[3] / a / div").text
    print(text)
    assert text == message


@then("Message about successful subscription is shown")
def step_impl(context):
    sleep(1.5)
    text = context.driver.find_element_by_xpath("/ html / body / section[9] / div / div / div[2] "
                                                "/div / div / div / div / span[3] / a / div").text
    print(text)
    assert text == "Thank you for subscription"
