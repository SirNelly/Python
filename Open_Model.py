import os.path
print("Open Model")
xDrive = "X:\\CAD DATA"
jDriveTemp = "J:\\"
assy = "null"
repeat = "y"

def prompt():
    prompt.kind = input("Model or Drawing: ")
    if "albion" in prompt.kind.lower():
        prompt.drive = "j"
        prompt.directory = str(input("Directory: "))
        prompt.kind = input('Model or Drawing: ')
        prompt.jDrive = (jDriveTemp + prompt.directory)
    else:
        prompt.drive = "x"
    prompt.pnTemp = input("Part Number: ")

def checkType():
    if "m" in prompt.kind.lower():
        checkType.fileType = "model"
    else:
        if "d" in prompt.kind.lower():
            if "model" in prompt.kind.lower():
                checkType.fileType = "model"
            else:
                checkType.fileType = "drawing"
        else:
            print("Please input File Type or check your spelling, you typed " + prompt.kind)
            
def drivePath():
    if "j" in prompt.drive:
        drivePath.drive = (prompt.jDrive + "\\")
    else:
        drivePath.drive = (xDrive + "\\")

def extensions():
    if "model" in checkType.fileType:
        if os.path.isfile(drivePath.drive + prompt.pnTemp + ".sldasm"):
            extensions.pn = (prompt.pnTemp + ".sldasm")
        else:
            extensions.pn = (prompt.pnTemp + ".sldprt")
    if "drawing" in checkType.fileType:
        if "cg" in prompt.pnTemp.lower():
            extensions.pn = (prompt.pnTemp + ".000.slddrw")
        else:
            extensions.pn = (prompt.pnTemp + ".slddrw")
    extensions.filePath = (drivePath.drive + extensions.pn)

while "y" in repeat.lower():
    prompt()
    checkType()
    drivePath()
    extensions()
    
    if os.path.isfile(extensions.filePath) == True:
        os.startfile(extensions.filePath)
        repeat = "n"
    else:
        print(extensions.pn + " Doesn't Exist")
        repeat = input("Try Again? (Y/N) ")
