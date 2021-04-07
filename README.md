# CONTL_Automated_Tests
Automated testing scripts with selenium and pytest for Continental Hotel

# Required installations
- Java 8 or higher for Allure reports
- Allure Framework

# Python packages used
- selenium
- pytest
- allure-pytest

# Considered Improvements 
- Rewrite all tests using POM design pattern
- Use webdriver-manager python package to programmatically set up webdriver at runtime

# How to use 

Use pytest
- pytest -v -s CONTL_Website_Tests\CONTL_ ... - press tab for autocomplete

To generate allure reports

1. pytest -v -s --alluredir="[path]"CONTL_Website_Tests\CONTL_ ... - press tab for autocomplete
 [path] = Allure_Reports
3. save report dir path, or open cmd in the directory with the report dir
4. run command: allure serve [dir path] or allure serve [dir with report name]
