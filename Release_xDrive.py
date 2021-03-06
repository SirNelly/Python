import os.path
import time
from shutil import copy2
from shutil import move

xDrive = "X:\Document Control\Colson Group Drawings"
oldRevX = (xDrive + "\Old Revisions")
desktop = "C:\\Users\\nelson.wagner\\Desktop"
printUpdates = (desktop + "\\Print Updates")
documents = "C:\\Users\\nelson.wagner\\Documents"
output = (desktop + "\\output.txt")
printInfo = []
printList = []
run = "y"

class Drawing:
    def __init__(self, pn, oldRev, newRev, typo, newRelease):
        self.pn = pn
        self.oldRev = oldRev
        self.newRev = newRev
        self.typo = typo
        self.newRelease = newRelease
        if "cg" in self.pn.lower():
            self.pn = (self.pn + ".000")
    def oldPrompt(self):
        self.oldRev = input("Old Revision Letter: ")
    def newPrompt(self):
        self.newRev = input("New Revision Letter: ")
    def revPrompt(self):
        self.oldPrompt()
        self.newPrompt()
    def typoCheck(self):
        if self.oldRev == self.newRev:
            self.typo = input("Your Revisions Are The Same, Is This Correct? (Y/N) ")
            while "n" in self.typo.lower():
                print("Please Check Your Revisions")
                self.revPrompt()
                if self.newRev == self.oldRev:
                    continue
                else:
                    self.typo = "y"
                    break
    def pnPrompt(self):
        self.pn = input("Part Number: ")
    def fullPrompt(self):
        self.pnPrompt()
        self.revPrompt()
    def Release(self):
        if "y" in self.newRelease.lower():
            copy2(newPaths.newPrintPath, xDrive)
        else:
            if "y" in self.typo.lower():
                os.remove(oldPaths.oldPrintPath)
                copy2(newPaths.newPrintPath, xDrive)
            else:
                move(oldPaths.oldPrintPath, oldRevX)
                copy2(newPaths.newPrintPath, xDrive)
        print(self.pn + " Has Been Released")

def newPaths():
    newPaths.newPrint = (object.pn + "_" + object.newRev + ".pdf")
    newPaths.newPrintPath = (printUpdates + "\\" + newPaths.newPrint)

def oldPaths():
    oldPaths.oldPrint = (object.pn + "_" + object.oldRev + ".pdf")
    oldPaths.oldPrintLegacy = (object.pn + ".pdf")
    oldPaths.oldPrintPath = (xDrive + "\\" + oldPaths.oldPrint)
    oldPaths.oldPrintLegacyPath = (xDrive + "\\" + oldPaths.oldPrintLegacy)

def pnPrompt():
    pnPrompt.pn = input("Part Number: ")
    pnPrompt.oldRev = input("Old Revision Letter: ")
    pnPrompt.newRev = input("New Revision Letter: ")  

while "y" in run.lower():
    pnPrompt()
    tempDrawing = Drawing(pnPrompt.pn, pnPrompt.oldRev, pnPrompt.newRev, "first", "first")
    tempDrawing.typoCheck()
    printList.append(tempDrawing)
    run = input("More Drawings? (Y/N) ")

for object in printList:
    newPaths()
    oldPaths()
    while os.path.isfile(newPaths.newPrintPath) == False:
        print(newPaths.newPrint + " Doesn't Exist, Please Check Your Spelling")
        object.pnPrompt()
        object.newPrompt()
        newPaths()
    while os.path.isfile(oldPaths.oldPrintPath) == False:
        if os.path.isfile(oldPaths.oldPrintLegacyPath) == True:
            oldPaths.oldPrint = oldPaths.oldPrintLegacy
            oldPaths.oldPrintPath = oldPaths.oldPrintLegacyPath
            break
        object.newRelease = input("Is This A New Release? (Y/N) ")
        if "n" in object.newRelease.lower():
            print(oldPaths.oldPrint + " Doesn't Exist")
            object.oldPrompt()
            oldPaths()
        if "y" in object.newRelease.lower():
            break
    object.Release()
    time.sleep(0.5)
