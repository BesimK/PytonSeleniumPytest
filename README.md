# Selenium Page Object Model with Singleton Driver

Welcome to the Selenium Page Object Model (POM) demonstration project. This project showcases the application of the Page Object Model design pattern using Selenium WebDriver in Python. It is designed to offer an organized and scalable approach to automated web testing.

## Overview

Automated testing is a critical component of modern software development, enabling teams to validate application functionality efficiently and reliably. The Page Object Model (POM) is a popular design pattern that enhances test maintainability, readability, and reusability by encapsulating web page elements and their interactions into reusable components called page objects.

## Features

- **Singleton WebDriver Manager**: The project implements a singleton WebDriver manager, ensuring that a single WebDriver instance is shared across multiple tests, thus reducing resource consumption and improving test execution speed.
  
- **Configuration Management**: The configuration settings are managed centrally, allowing easy customization and adjustment of test parameters such as browser type, URL, timeouts, etc.
  
- **Base Page Class**: The base page class serves as the foundation for all page objects. It encapsulates common functionality and utility methods for interacting with web elements, such as clicking buttons, entering text, retrieving element properties, etc.
  
- **Reusable Page Objects**: Each page of the web application is represented as a separate page object, containing locators and methods specific to that page. This modular approach facilitates easy maintenance and updates as the application evolves.
  
- **Parallel Test Execution**: To run tests in different browsers concurrently, use the `Runner.py` script provided in the project.

## Project Structure

The project follows a structured layout to promote organization and clarity:

- **`config.py`**: This module contains configuration settings such as browser type, base URL, timeouts, etc.
  
- **`driver_manager.py`**: The singleton WebDriver manager responsible for instantiating and managing the WebDriver instance.
  
- **`base_page.py`**: The base page class encapsulates common functionality and utility methods shared by all page objects.
  
- **`pages/`**: This directory contains individual page objects, each representing a specific page of the web application. Each page object contains locators and methods for interacting with elements on that page.
  
- **`tests/`**: Test scripts are organized into this directory. Each test script instantiates page objects and performs actions/tests specific to the corresponding pages.
  
- **`Runner.py`**: Use this script to run tests in parallel across different browsers.

## Getting Started

To get started with the project:

1. Clone the repository to your local machine.
2. Install the necessary dependencies listed in `requirements.txt`.
3. Customize the configuration settings in `config.py` as per your requirements.
4. Write your test scripts in the `tests/` directory, utilizing the provided page objects.
5. Use the `python Runner.py` script to run tests in parallel across different browsers.

## Contributions

Contributions to the project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
