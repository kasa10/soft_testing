
Feature: Sign up page test

Background:
    Given The PHPTravels sign up page is open

  Scenario Outline: Create a User using valid data
    Given Verify registration page
    When The user record has a first name of "<fname>"
    And the user record has a last name of "<lname>"
    And Mobile Phone is "<phone>"
    And Enter email "<email>"
    And Password of "<password>"
    And Signup button click
    Then The user must successfully create an account
    Examples:
      | email                  | fname  | lname      | password  |   phone  |
      | ivanov123@gmail.com       | bjarne | stroustrup | 5678910   |  5876657 |
      | petrov123@mail.ru         | james  | gosling    | 5978910   |  9676687 |
      | python123@yandex.ru       | guido  | rossum     | 5678999   |  3876656 |
      | example159@email.com   | larry  | wall       | 3278910   |  1276654 |



  Scenario: Already registered user registration
    Given Verify registration page
    When The user record has a first name of "bjarne"
    And the user record has a last name of "stroustrup "
    And Mobile Phone is "5876657"
    And Enter email "ivanov123@gmail.com"
    And Password of "5678910"
    And Signup button click
    Then The user get message that user already exist
