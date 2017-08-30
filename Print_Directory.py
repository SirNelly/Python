import os.path
print("Print Directory")
folder = input("Which Folder? ")
desktop = "C:\\Users\\nelson.wagner\\Desktop"
output = (desktop + "\\" + folder + ".txt")
j = "J:\\"
jDrive = (j + folder)

a = open(output, "w")
for path, subdir, files in os.walk(jDrive):
    for filename in files:
        f = os.path.join(filename)
        a.write(str(f) + os.linesep)
os.startfile(output)
