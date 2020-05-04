import PythonMagick
import os
 
path = os.getcwd()
filename = input("2.png")
filepath = path + '//' + filename
 
img = PythonMagick.Image(filepath)
img.sample('128x128')
 
newpath = path + '//ico.ico'
img.write(newpath)
