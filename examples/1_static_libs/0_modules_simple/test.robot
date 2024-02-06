*** Settings ***
Library    my_lib.py
Library    Collections

*** Test Cases ***
Test Monday
    ${Result}=    My Favourite Keyword    Monday
    Should Be Equal    ${Result}    Blah

Test Tuesday
    ${Result}=    My Favourite Keyword    Tuesday
    Should Be Equal    ${Result}    Waiting for friday

Test Colour
    ${Colour}=    My Favourite Colour    Monday    
    Should Be Equal    ${Colour}    Pink

Test Multiple Arguments
    @{Persons}=    Create List    Dan    Philipp
    ${Result}=    Favourite Colours    Monday    ${Persons}
    Log To Console    ${Result}

Test Named Arguments
    ${Out}=    Favourite Drinks    7 am    Claudio
    Log To Console    ${Out}
    ${Out}=    Favourite Drinks    name=Dan    time=4 am in Maryland
    Log To Console    ${Out}

Test Keyword Arguments
    ${Out}=    Favourite Drinks    2 pm    Philipp
    ...    season=winter    mood=good
    Log To Console    ${Out}
    
Test Named Only Args
    # My Keyword Only Named Args    arg1=hello    arg2=world
    My Keyword Only Named Args    hello    world

Test Multi Return
    ${Ret1}    ${Ret2}=    Keyword Multi Return
    Log To Console    ${Ret1}
    Log To Console    ${Ret2}
    
    @{All returns}=    Keyword Multi Return
    Log To Console    ${All returns}
    FOR    ${element}    IN    @{All returns}
        Log To Console    ${element}
    END

Test Visibility
    # Expected to fail
    My Special Function