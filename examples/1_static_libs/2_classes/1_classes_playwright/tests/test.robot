*** Settings ***
Resource            ../keywords/common.resource

Test Setup          Launch Sausedemo
Test Teardown       Close Sausedemo


*** Test Cases ***
Test one
    Open Login Page
    Open Log File
