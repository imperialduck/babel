"""
UTILS.PY
Catalog shared fuctions
"""


def get_century(year):
    """[returns century based on year]
    
    Returns:
        [int]
    """

    year = int(year)
    if year > 100:
        century = year % 100
        if century == 0:
            century = year // 100
        else:
            century = year // 100 + 1
    else:
        century = 1

    return century
