# CONTL_Automated_Tests
Automated testing scripts with selenium and pytest for Continental Hotel

# Generated Allure Report

Check it here -> # https://contl-allure-generated-report.netlify.app/
![image](https://user-images.githubusercontent.com/70851317/114315450-c0ffd480-9b07-11eb-8ad0-3dc13d61e17d.png)
![image](https://user-images.githubusercontent.com/70851317/114315469-cd842d00-9b07-11eb-8138-dbc15cd8c4ed.png)


# Required installations
- Java 8 or higher for Allure reports
- Allure Framework - https://docs.qameta.io/allure/#_installing_a_commandline

# Python packages used
- selenium - https://selenium-python.readthedocs.io/
- pytest
- allure-pytest

# Considered Improvements 
- Rewrite all tests using POM design pattern
- Use webdriver-manager python package to programmatically set up webdriver at runtime - https://pypi.org/project/webdriver-manager/

# How to use 

Use pytest
- pytest -v -s CONTL_Website_Tests\CONTL_ ... - press tab for autocomplete

To generate allure reports
- open terminal in IDE
1. pytest -v -s --alluredir="[path]"CONTL_Website_Tests\CONTL_ ... - press tab for autocomplete
 [path] = Allure_Reports
3. save report dir path, or open cmd in the directory with the report dir
4. run command: allure serve [dir path] or allure serve [dir with report name]
