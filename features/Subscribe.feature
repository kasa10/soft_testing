
Feature: Subscribe field test

  
  
  Background:
    Given The main page is open

  Scenario Outline: Subscribe with invalid email
    Given Subscribe field is displayed
    When Enter "<email>"
    And Click Subscribe button
    Then Get error "<message>"
    Examples:
      | email                     | message |
      |   N/A                     | Please add email!            |
      | 12312141                  | Please add correct email!    |
      | mailbox123                | Please add correct email!    |
      | @mail.ru                  | Please add correct email!    |



  Scenario:  Subscribe with valid email
    Given Subscribe field is displayed
    When Enter "example1@mail.ru"
    And Click Subscribe button
    Then Message about successful subscription is shown
