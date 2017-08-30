import os.path
from shutil import copy2
from shutil import move

xDrive = "X:\Document Control\Colson Group Drawings"
printUpdates = "C:\\Users\\nelson.wagner\\Desktop\\Print Updates"
desktop = "C:\\Users\\nelson.wagner\\Desktop"
output = (desktop + "\\output.txt")
ticker = 0
ticker2 = 0
delete = []
deletePath = []

a = open(output, "w")
for path, subdirs, files in os.walk(r'C:\users\nelson.wagner\Desktop\Print Updates'):
    for filename in files:
        f = os.path.join(filename)
        a.write(str(f) + os.linesep)

with open(output) as a:
    updates = a.readlines()
updates = [x.strip() for x in updates]

prints = len(updates)
prints -= 1

while ticker <= prints:
    drawing = updates[ticker]
    drawingPath = (xDrive + "\\" + drawing)
    if os.path.isfile(drawingPath) == True:
        delete.append(drawing)
        deletePath.append(printUpdates + "\\" + drawing)
    ticker += 1
print("Action will delete", delete)
go = input("Proceed? (Y/N) ")

removals = len(delete)
removals -= 1

if "y" in go.lower():
    while ticker2 <= removals:
        os.remove(deletePath[ticker2])
        ticker2 += 1
os.remove(output)
