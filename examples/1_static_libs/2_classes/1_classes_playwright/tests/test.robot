*** Settings ***
Resource            ../keywords/common.resource

Test Setup          Launch Sausedemo
Test Teardown       Close Sausedemo


*** Test Cases ***
Test one
    Login    standard_user    secret_sauce
    # Check Backpack Shown    Sauce Labs XYZ
    Prüfe den Rucksack    backpack_name

Test two
    Logging Example Keyword

Test visibility
    # Expected to fail
    Invisible Function