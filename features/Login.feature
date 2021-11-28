
Feature: Login test


  Background:
    Given The PHPTravels site is open
    And The Login link is clicked


  Scenario:  Login with incorrect credentials
    Given Enter email "asdfghjkl@mail.ru" and password "123"
    When Login button is clicked
    Then The error message is shown




  Scenario Outline: Fail Login
    Given Enter email "<mail>" and password "<password>"
    When Login button is clicked
    Then Text field error is shown
    Examples:
      | mail          | password |
      |               | 123      |
      | example123    | 12345    |
      | asdf@mail.ru  |          |
      |               |          |




    Scenario:  Successful login
      Given Enter email "ivanov123@gmail.com"
      And Password of "5678910"
      When Login button is clicked
      Then Page of user's account is opened