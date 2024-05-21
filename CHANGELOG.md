# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- DriverManager class to handle WebDriver instances with singleton pattern.
- ConfigManager class to read configuration settings from configuration.properties.
- BasePage class with various helper methods for interacting with web elements.
- Configuration settings for browser type in configuration.properties.

### Changed
- Updated DriverManager to read browser type from ConfigManager.
- Enhanced BasePage with additional helper methods for improved interaction with web elements.

## [1.0.0] - 2024-05-20

### Added
- Initial implementation of the project.
- Basic structure with DriverManager, ConfigManager, and BasePage classes.