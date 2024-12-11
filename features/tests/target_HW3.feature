# Created by esobeokeh at 12/11/24

Feature: Cart icon test

  Scenario: User can click and open the cart icon
    Given Open target main page
    When CLick cart icon
    Then Verify cart icon opens and is empty


# Feature: Sign in page test

  Scenario: Logged out user can navigate to sign in page
    Given Open target main page
    When Click sign button on the right top corner
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened