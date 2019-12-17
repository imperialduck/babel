from second import validate
from second import F_ERROR
print("THIRD")
d = validate("Emmanuel10 G. Sandorfi")
if F_ERROR in d:
    print(d[F_ERROR])
print(d)
