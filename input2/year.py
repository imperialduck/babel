# Year of birth management

import datetime

DATE = datetime.datetime.now()


def validate_year(year):
    """
    {
        year: STRING
    }
    Validates that a string is convertible to INT and converts it
    Then, checks if year is 2 digits and converts it to a 4 digits date if its not in the future
    """
    length = len(str(year))
    try:
        int(year)
    except Exception:
        print("L'année de naissance ne doit comporter que des chiffres")
        year = None
        return year
    else:
        year = int(year)
        if length <= 2:
            year = check_age(year)
        elif year > DATE.year:
            year = None
            print("Nom de Zeus ! Marty, nous sommes revenus en {}".format(DATE.year))
        return year


def check_age(year):
    """
    {
        year: INT
    }
    If the two digits date entered is at most 20 years old and not in the future, place it in the 1900's
    Else, place it in the 2000's
    """
    if (year + 1900) >= (DATE.year - 20) or ((year + 2000) > DATE.year):
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

        user_input = validate_year(user_input)
        if input_len == 2 or input_len == 4:
            if user_input:
                return user_input
            else:
                user_input = ''
        else:
            print("Erreur, votre année de naissance doit comporter 2 ou 4 chiffres")
            user_input = ''


if __name__ == "__main__":
    a = controller_input()
    print(a)
