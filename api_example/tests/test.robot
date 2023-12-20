*** Settings ***
Library    ../libs/employees_api/employees_api.py

*** Test Cases ***
Check All Employees
    ${Everyone}=    Get All Employees
    Log    ${Everyone}