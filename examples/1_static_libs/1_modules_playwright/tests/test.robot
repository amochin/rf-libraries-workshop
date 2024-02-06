*** Settings ***
Library             ../libs/sausedemo.py

Test Setup          Launch Sausedemo
Test Teardown       Close Sausedemo

*** Test Cases ***
Simple Login
    Login    standard_user    secret_sauce
    No Operation

Check backpack
    Login    standard_user    secret_sauce
    Check Backpack Shown    Sauce Labs Backpac
    Log To Console    I shouldn't have come here normally