import os

swPath = "C:\\Program Files\\SOLIDWORKS Corp\SOLIDWORKS\\SLDWORKS.exe"
olPath = "C:\\Program Files\\Microsoft Office\\Office14\\OUTLOOK.exe"
refPath = "X:\\Shared Data\\Polyurethane\\Tracking Document\\Reference Documents"
ftpPath = (refPath + "\\FTP_Collector.xlsx")
xDrivePath = (refPath + "\\X_Drive_Collector.xlsx")

os.startfile(swPath)
os.startfile(olPath)
os.startfile(ftpPath)
os.startfile(xDrivePath)