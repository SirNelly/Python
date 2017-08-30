import os.path
from shutil import copy2
print("Print ECN")
ecnPath = "S:\\Nelson\\ECN's"
xDrive = "X:\\Document Control\\ECN\\2017"

year = "017"

ecnTemp = input("ECN Number: ")
ecn = (ecnTemp + "-" + year)

copy2((ecnPath + "\\" + ecn), xDrive)
