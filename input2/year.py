# Year of birth management

import datetime


def is_int(number):
    """
    Check if a given string can be converted to a number
    """
    a = False
    try:
        int(number)
    except:
        pass
    else:
        a = True
    return a


def check_age(year):
    """
    Takes in an INT as year
    If the two digits date entered is 20 years old and not in the future, place it in the 1900's
    Else, place it in the 2000's
    """
    date = datetime.datetime.now()
    if (year + 1900) >= (date.year - 20) or ((year + 2000) > date.year):
        return year + 1900
    else:
        return year + 2000


def strip_zeros(two_dig_date):
    """
    Strips every zero beginning a two digits date
    """
    two_dig_date = two_dig_date[1]  # Strip the 0 at the beginning any two digits date so it can be converted to int
    return two_dig_date


def controller_input():
    """
    While the input is deemed invalid,
    it will be set back to empty
    And the function will loop
    """
    user_input = ''
    while user_input == '':
        user_input = input("Entrez votre année de naissance (format yy ou yyyy)")
        input_len = len(user_input)
        if user_input[0] == "0":
            user_input = strip_zeros(user_input)

        if is_int(user_input):
            user_input = int(user_input)
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
