import os
import shutil

fileNames = []
for name in os.listdir ():
    if os.path.isfile (name):
        fileNames.append (name)

dirNames = []
for name in os.listdir ('simulations'):
    if os.path.isdir (os.path.join ('simulations', name)):
        dirNames.append (name)

print ()        
    
print ('fileNames:')
for fileName in fileNames:
    print (fileName)
print ()
    
print ('dirNames:')
for dirName in dirNames:
    print (dirName)
print ()
            
for fileName in fileNames:
    if fileName == 'build.py':
        continue
        
    for dirName in dirNames:        
        if fileName == 'rename.ino':
            targetFileName = dirName + '.ino'
        else:
            targetFileName = fileName
              
        targetPath = os.path.join ('simulations', dirName, targetFileName)
              
        print ('Copying', fileName, 'to', targetPath)
        shutil.copyfile (fileName, targetPath)
        
for dirName in dirNames:
    os.chdir (os.path.join ('simulations', dirName))
    os.system ('compile')
    os.chdir (os.path.join ('..', '..'))