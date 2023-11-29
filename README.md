# Python Testing Repository ![Status](https://img.shields.io/badge/status-work_in_progress-important)

## Overview

This repository is a resource for different types of testing in Python. It includes example Flask web application, examples for Robot Framework, and Python's built-in `unittest` framework.

## Contents

- **flask/**: Contains a Flask web application that can be used to test web-automation.
- **robotframework/**: Includes examples of acceptance testing using Robot Framework, an open-source automation framework for acceptance testing and RPA (Robotic Process Automation).
- **unittest/**: Provides examples for using Python's built-in `unittest` framework for writing and running unit tests.

## What is Testing?

Testing in software development is the process of evaluating software to verify that it meets the required results. It's crucial for ensuring software quality, finding and fixing bugs, and validating that the software is fit for use.

## Types of Testing

- **Unit Testing**: Testing individual components or pieces of code for correctness. Typically, this is done at the function level.
- **Integration Testing**: Testing the interaction between integrated units/modules as a group.
- **Acceptance Testing**: Testing the entire application in a real-world scenario to ensure it meets the business requirements.

## Getting started

Clone the repository to your own machine using git

```sh
git clone https://github.com/rikurampanen/python-testing
```

### Setting Up a Virtual Environment

To isolate the testing environment, it's recommended to use virtual environment:

```sh
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

### Installing Dependencies

To install dependencies, run:

```sh
pip install -r requirements.txt
```

## Useful Links

- **Flask**: [Flask Documentation](https://flask.palletsprojects.com/)
- **Robot Framework**: [Robot Framework User Guide](https://robotframework.org/)
- **Unittest**: [Python Unittest Documentation](https://docs.python.org/3/library/unittest.html)

## Contributing

Contributions to this repository are welcome. Please adhere to the guidelines set forth in each subfolder's README.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
