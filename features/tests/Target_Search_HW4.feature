
Feature: Target search tests
  Scenario: User can search for tea
  Given Open target main page
  When Search for tea
  Then Verify search result is shown for tea


  Scenario: User can search for gun
  Given Open target main page
  When Search for gun
  Then Verify search result is shown for gun


  Scenario: User can search for shampoo
  Given Open target main page
  When Search for shampoo
  Then Verify search result is shown for shampoo


#Feature: Target Circle page test
  Scenario: User can see the Target benefit cells
    Given Open target main page
    When Click target circle icon
    Then Verify atleast 10 benefit cells shown


#Feature: Adding Target’s product into the cart tests
  Scenario: User can add products into cart
    Given Open target main page
    When Search for tea
    And Click on Add to cart
    And Click on the Add to Cart on the side bar
    And Open cart page
    Then Verify Tea is in cart




