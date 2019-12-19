"""
Setup v0.1 programme qui affiche le setup de la machine python
Changelog:
    - example changelog 12/18/2019
    - second line
    - Corrected stupid stuff written in changelog
    - This actually is stupid stuff
    - I should just stop now
"""

import sys
import os
import datetime


def printseparator():
    """
    Fonction qui affiche une ligne de séparation
    """
    print('-' * 50)


print(sys.executable)
print(sys.platform)
print(sys.path)

v = sys.version_info

print(type(v))
print(dir(v))

# print(f"Python version {v.major}.{v.minor}.{v.micro}")
print("Python Version {}.{}.{}".format(v.major, v.minor, v.micro))
print("Environment PythonPath : " + os.getenv("PYTHONPATH", "Vide"))
print(datetime)
print(datetime.__file__)

dt = datetime.datetime.now()
