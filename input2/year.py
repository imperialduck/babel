# Year of birth management

import datetime


def validate_year(year):
    """
    {
        year: STRING
    }
    Validates that a string is convertible to INT and converts it
    """
    try:
        int(year)
    except Exception:
        year = None
        return year
    else:
        year = int(year)
        return year


def check_age(year):
    """
    {
        year: INT
    }
    If the two digits date entered is at most 20 years old and not in the future, place it in the 1900's
    Else, place it in the 2000's
    """
    date = datetime.datetime.now()
    if (year + 1900) >= (date.year - 20) or ((year + 2000) > date.year):
        return year + 1900
    else:
        return year + 2000


def controller_input():
    """
    While the input is deemed invalid, it will be set back to empty allowing the function to loop
    """
    user_input = ''
    while user_input == '':
        user_input = input("Entrez votre année de naissance (format yy ou yyyy)")
        input_len = len(user_input)
        if user_input[0] == "0" and input_len >= 2:
            user_input = user_input[1]  # Strip the 0 at the beginning of the string as it will prevent any conversion to INT and crash the program

        user_input = validate_year(user_input)
        if user_input:
            if input_len == 2:
                user_input = check_age(user_input)
                return user_input
            elif input_len == 4:
                return user_input
            else:
                print("Erreur, votre année de naissance doit comporter 2 ou 4 chiffres")
                user_input = ''
        else:
            print("L'année de naissance ne doit comporter que des chiffres")
            user_input = ''


if __name__ == "__main__":
    a = controller_input()
    print(a)
