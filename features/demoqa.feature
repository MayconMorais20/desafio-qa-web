Feature: DemoQA Forms Page

  Scenario: Verify presence of "Forms" text on DemoQA website
    Given I open the DemoQA website
    And I click on the Form
    And I fill all the fields with random data
    And I submit the form
    When I should see a pop-up message
    Then I close the pop-up