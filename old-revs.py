import os.path
import glob
from shutil import move

xDrive = "X:\\Document Control\\Colson Group Drawings"
oldRev = (xDrive + "\\Old Revisions")
desktop = "C:\\Users\\nelson.wagner\\Desktop"
pn = (desktop + "\\Temp.txt")
output = (desktop + "\\Old_Revs.txt")

with open(pn) as f:
    pn = f.readlines()
pn = [x.strip() for x in pn]
oldRevList = []

for x in pn:
    drawing = pn[x]
    drawingPath = (xDrive + "\\" + drawing + "*.pdf")
    oldRevList.extend(glob.glob(drawingPath))

for x in pn:
    drawing = pn[x]
    drawing2 = oldRevList[x]
    oldRevPath = (oldRev + "\\" + drawing + "*.pdf")
    if os.path.isfile(oldRevPath):
        print("Duplicate")
    else:
        move(drawing2, oldRev)
        print("Moved " + oldRevList[moved])