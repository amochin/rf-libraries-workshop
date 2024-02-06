*** Settings ***
Library    examples.1_static_libs.2_classes.0_classes_simple.MyLib

*** Test Cases ***
Test One
    ${res}=    My Keyword    Hello!
    Log To Console    ${res}