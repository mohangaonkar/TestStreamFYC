Feature: Automate video player functionality on FYC platform

  Scenario: Sign in and navigate through the platform
    Given I navigate to the FYC platform
    When I sign in with the provided PIN
    Then I should be logged into the platform

  Scenario: Navigate to the Test Automation Project page
    When I scroll to All Titles
    When I click on the "Test Automation Project"
    Then I should be navigated to the project page

  Scenario: Play video and perform video interactions
    When I scroll to Test Automation Project
    When I switch to the "Details" tab
    When I return to the "Videos" tab
    When I play the video
    Then the video should play for 10 seconds
    When I click the "Pause" button
    When I click the "Continue Watching" button

  Scenario: Adjust volume to 50%
    When I adjust the volume to 50%
    Then the volume level should be set to 50%

  Scenario: Change video resolution to 480p
    When I open the settings menu and change the resolution to 480
    Then the resolution should be updated to "480p"

  Scenario: Change video resolution to 720p
    When I change the video resolution to "720p"
    Then the resolution should be updated to "720p"

  Scenario: User signs out successfully
    When I click on the Pause video
    And I click on the Back button
    Then I should be redirected to the previous screen
    When I click on the Signout button
    Then I should be logged out successfully
