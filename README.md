# BABEL

### What is this project ?
This is a simple student project, bound to have many flaws, and created for learning purposes.

## setup.py file

This file contains boilerplate functions to constantly check the system
It will be useful to check :
- Your Python version
- Your executable path
- Today's date
Also the print separator function allows  you to quickly draw a line between two blocks to improve readability during development

## input.py file

This file contains code to ask the user to enter his name

## second.py

Most of our code is listed here :
- The validate_display function is kinda deprecated, but it takes in the user input and breaks it down in First name, middle name and last name before displaying it
- The validate function makes sure the name is comprised only of 3 names (first, middle, last) and does not contain digits or special characters  
it takes in a string and returns a boolean
```python
if (validate("John Doe")):
    ...
```
- The manage input function is here for testing purposes and does as much as what the input.py file does

## third.py

Testing file to write unit tests