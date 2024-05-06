*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  tiina  tiina123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username must contain at least 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle3  kalle123
    Output Should Contain  Username can contain only letters

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle
    Output Should Contain  Password must contain at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekoi
    Output Should Contain  Password must contain at least 1 character that isn't a letter

*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command