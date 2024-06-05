@all
Feature: Sample Scenario
  @test
  Scenario: Sample Test
    Given I do something
    When I do another thing
    Then I should be OK
  @wiki  
  Scenario:Wiki Test
    Given user is navigated to Wikipedia
    When user makes a search for "Gang Of Four"
    Then user should see "Gang Of Four"