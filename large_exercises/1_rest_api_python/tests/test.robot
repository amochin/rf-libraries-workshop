*** Settings ***
Library    ../libs/employees_api/employees_api.py

*** Test Cases ***
Check All Employees
    ${Everyone}=    Get All Employees
    Log    ${Everyone}

Check Employee
    ${Res}=    Get Employee Data    1
    Log To Console    ${Res}