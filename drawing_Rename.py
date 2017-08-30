import os.path
from shutil import copy2
from shutil import move

desktop = "C:\\Users\\nelson.wagner\\Desktop"
printUpdates = (desktop + "\\Print Updates")
output = (printUpdates + "\\output.txt")
newRev = "null"
pn = "null"
pnPath = "null"
oldPath = "null"

a = open(output, "w")
for path, subdirs, files in os.walk(r'C:\Users\nelson.wagner\Desktop\Print Updates'):
    for filename in files:
        f = os.path.join(filename)
        a.write(str(f) + os.linesep)
with open(output) as a:
    drawingRaw = a.readlines()
drawingRaw = [x.strip() for x in drawingRaw]

ticker = 0
scrap = []
drawing = []
drawings = len(drawingRaw)
drawings -= 1
y = "null"

while ticker <= drawings:
    item = str(drawingRaw[ticker])
    if "_" in item:
        scrap.append(item)
    else:
        if "-" in item:
            scrap.append(item)
        else:
            if ".txt" in item:
                scrap.append(item)
            else:
                drawing.append(item)
    ticker += 1

ticker = 0
drawing = list(filter(None, drawing))
drawings = len(drawing)
drawings -= 1
z = "null"
size = "null"

while ticker <= drawings:
    x = str(drawing[ticker])
    z = x.rsplit('.',1)[0]
    z = list(z)
    size = len(z)
    size -= 1
    newRev = z[size]
    size -= 1
    z = z[:-1]
    pn = ''.join(z)
    if "cg" in pn.lower():
        pn = (pn + ".000")
    pn = (pn + "_" + newRev + ".pdf")
    oldPath = (printUpdates + "\\" + x)
    pnPath = (printUpdates + "\\" + pn)
    os.rename(oldPath, pnPath)
    ticker += 1
os.remove(output)
