import os
import os.path
import glob
import time

print("Open Drawing")
xDrive = "X:\\Document Control\\Colson Group Drawings"
dnTemp = input("Drawing Number: ")
dn = "null"
dnPrint = "null"

if "cg" in dnTemp.lower():
    dn = (dnTemp + ".000_*.pdf")
else:
    dn = (dnTemp + "_*.pdf")

dnPath = (xDrive + "\\" + dn)

printlist = [glob.glob(dnPath)]

if not printlist:
    dn = (dnTemp + "*.pdf")
    dnPath = (xDrive + "\\" + dn)
    printlist = [glob.glob(dnPath)]
    if not printlist:
        print("Drawing Doesn't Exist: " + dn)
        time.sleep(1.0)

if printlist:
    dnPrint = dnPath

for filename in glob.glob(dnPrint):
    os.startfile(filename)
