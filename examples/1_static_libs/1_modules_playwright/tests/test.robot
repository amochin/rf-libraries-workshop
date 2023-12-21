*** Settings ***
Library             ../libs/sausedemo.py

Test Setup          Launch Sausedemo
Test Teardown       Close Sausedemo

*** Test Cases ***
Simple Login
    No Operation