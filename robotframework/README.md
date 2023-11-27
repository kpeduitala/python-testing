# Robot Framework

## Description

This project uses Robot Framework, an open-source automation framework for acceptance testing, acceptance test-driven development (ATDD), and robotic process automation (RPA). Robot Framework is keyword-driven and utilizes easy-to-read syntax.

## Features

- Automated Acceptance Tests: Write tests in a human-readable format.
- Keyword-Driven Testing: Use existing keywords or create custom ones.
- Extensible: Extend the framework with Python or Java libraries.
- Integration: Integrates with various tools for continuous integration and testing.

## Writing Tests

Tests in Robot Framework are written in simple text files:

- Create a new `.robot` file in the `tests` directory.
- Use the **_Settings_**, **_Variables_**, **_Test Cases_**, and **_Keywords_** sections to structure your test.

### example.robot

```robot
*** Settings ***
Documentation     A simple test with Robot Framework and Selenium.
Library           SeleniumLibrary

*** Test Cases ***
Open And Verify Example Website
    [Documentation]    Opens a web browser and checks the title of 'http://example.com'.

    # Open the browser
    Open Browser    http://example.com    browser=Chrome

    # Check the title of the page
    Title Should Be    Example Domain

    # Close the browser
    Close Browser
```

### Explanation:

    Settings Section:
        Documentation: Provides a description of what this test suite does.
        Library: Includes the SeleniumLibrary, which is necessary for web testing with Selenium.

    Test Cases Section:
        Open And Verify Example Website: The name of the test case.
            [Documentation]: A description of what this specific test case does.
            Open Browser: A keyword from SeleniumLibrary that opens a browser and navigates to the specified URL. Replace Chrome with the browser you intend to use (e.g., Firefox, Edge).
            Title Should Be: Another keyword that checks whether the current page's title matches the expected title.
            Close Browser: This keyword closes the browser window.

## Running Tests

To run tests, execute the following command in the project directory:

```sh
robot tests/
```

## Reporting

Robot Framework generates reports and logs in HTML format, providing detailed insights into the test execution.
