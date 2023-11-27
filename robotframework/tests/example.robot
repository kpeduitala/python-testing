*** Settings ***
Documentation     A simple test with Robot Framework and Selenium.
Library           SeleniumLibrary

*** Test Cases ***
Open And Verify Example Website
    [Documentation]    Opens a web browser and checks the title of 'http://google.com'.
    
    # Open the browser
    Open Browser    http://google.com    browser=Chrome
    
    # Check the title of the page
    Title Should Be    Google
    
    # Close the browser
    Close Browser