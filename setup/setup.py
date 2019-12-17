"""
Setup v0.1 programme qui affiche le setup de la machine python
Changelog:
    - dec 17 qkmdsqklmdsq
    - Je suis un petit champignon
"""

import sys
import os
import datetime


def printseparator():
    """
    Fonction qui affiche une ligne de séparation
    """
    print('-' * 50)


a = "dlqjdsl"
print(a)  # J'affiche l'objet

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

dt = datetime.now()
