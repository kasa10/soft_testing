from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import *
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


@given("The main page is open")
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.phptravels.net/")
    context.driver.maximize_window()
    WebDriverWait(context.driver, 10) #aaaa
    assert context.driver.title == "PHPTRAVELS - PHPTRAVELS"


@given("Verify page")
def step_impl(context):
    assert context.driver.title == "PHPTRAVELS - PHPTRAVELS"


@when("Enter city name")
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#hotels-search > div > div > div.col-md-4 > div > div > div > span > span.selection > span").click()
    context.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys("Debrecen")
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys(Keys.ENTER)
    sleep(1)


@step("Enter a check in date")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='checkin']").click()
    sleep(1)
    context.driver.find_element_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr[3]/td[4]").select() #december 2
    # context.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(26) > div.datepicker-days > table > tbody > tr:nth-child(2) > td:nth-child(1)").click()
    # WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable(
    #     (By.XPATH, "/html/body/div[2]/div[1]/table/tbody/tr[2]/td[1]"))).click()
    sleep(1)



@step("Enter a check out date")
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[3]/div[1]/table/tbody/tr[1]/td[7]").click() #december 4



@step("Add one child")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='hotels-search']/div/div/div[3]/div/div/div/a").click()
    sleep(1)
    context.driver.find_element_by_xpath(" //*[@id= 'hotels-search' ]/div/div/div[3]/div/div/div/div/div[3]/div/div/div[2]/i").click()
    sleep(1)


@step("Press Search button")
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='submit']").click()
    sleep(2)


@then("Page with available hotels will open")
def step_impl(context):
    text = context.driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div/div/div/span/strong/h2").text
    print(text)
    assert text == "Search Hotels In Debrecen"
