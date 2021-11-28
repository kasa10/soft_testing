
Feature: Contact Us page test

  Background:
    Given The main page is open
    And The Contact us link is clicked

 Scenario Outline: Enter Invalid data
    Given Verify that contact page is opened
    When The user enter name "<name>"
    And The user enter email "<email>"
    And The user enter message "<message>"
    # And Captcha click
    And Send button click
    Then Get error message
    Examples:
      | email                  | name              | message   |
      | example                | !!!               | 5678910   |
      | N/A                    | jsdss gsdfjsn     | 5978910   |
      | 4142142432424233322    | 23423342432322    | 5678999   |
      | %#@$!@                 | lsdkdy waldskfl   | 3278910   |




   Scenario: Enter Valid data
     Given Verify that contact page is opened
      When The user enter name "Ivan Ivanov"
      And The user enter email "example@gmail.com"
      And The user enter message "Hello world!"
      And Send button click
      Then Message sent successfully