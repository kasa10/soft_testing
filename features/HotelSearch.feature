
Feature: Verification of the hotel search on the website


  Background:
    Given The main page is open

  Scenario: Search with valid data
    Given Verify page
    When Enter city name
    And Add one child
    And Press Search button
    Then Page with available hotels will open


#  Scenario Outline: Search with invalid city
#    Given Verify page
#    When Enter city "<name>"
#    And Add "<number>" child
#    And Press Search button
#    Then Page with available hotels will open
#    Examples:
#      | name    | number |
#      | city    | 1      |
#      | 123     | 5      |
#      | !!!     | 3      |
#      | sjfbsj  | 2      |

