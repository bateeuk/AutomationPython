
Feature: Check the registration of a Car from the application
         In this feature a customer after login would search for
         the price of his vehicle and vehicle details

  Background:
    Given User open browser, enter URL and navigate to Free Car Check page
  Scenario Outline: Verify Registration Number with multiple "REG Number"
    When User enters Registration Number "REG Number"

  @Registration
  Scenario: Check the registration of used cars to verify the stipulated price and vehicle details
    When User clicks vehicle enquiry text field and enters "<REG Number>"
    And User selects the Free Car Check button
    Then User is directed to the Vehicle Identity screen
    And User checks and logs down the vehicle details
    Then User navigates back to the Free Car Check page

  Scenario Outline: Verify Registration Number with multiple "REG Number"
    When User enters Registration Number "REG Number"

  @Registration
  Scenario: Check the registration of used cars to verify the stipulated price and vehicle details
    When User clicks vehicle enquiry text field and enters "<REG Number>"
    And User selects the Free Car Check button
    Then User is directed to the Vehicle Identity screen
    And User checks and logs down the vehicle details
    Then User navigates back to the Free Car Check page


