number = int(input("Number of Prints: "))
arrayOfDrawings = ["null"]*number
class Drawing:
    def __init__(self, number, oldRevision, newRevision):
        self.number = number
        self.oldRev = oldRevision
        self.newRev = newRevision
for x in range(0, number):
    pn = input("PN: ")
    oldRev = input("Old Rev: ")
    newRev = input("New Rev: ")
    tempDrawing = Drawing(pn, oldRev, newRev)
    arrayOfDrawings[x] = tempDrawing
for object in arrayOfDrawings:
    print(object.number)
