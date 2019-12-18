import year


t_year = year.validate_year("1987")
print(t_year)
# expected output : 1987

t_year = year.validate_year(1987)
print(t_year)
# expected output : 1987

t_year = year.validate_year("qdkldsjq")
print(t_year)
# expected output : None