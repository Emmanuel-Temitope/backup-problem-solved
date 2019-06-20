# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 18:52:56 2019

@author: Emmanuel-Temitope
"""

import os
import time

#location of directory
source = [r'C:\Users\Emmanuel-Temitope\Documents\Coding\Python\Code\backup-solution', '"C:\\Users\\Oloyede Emmanuel"']

#targer directory
target_dir = r'C:\Users\Emmanuel-Temitope\Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    
today = target_dir + os.sep + time.strftime('%Y%m%d')
#current time will be the zip archive
now = time.strftime('%H%M%S')
#User Comment
comment = input('Enter a comment --> ')
#check if comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(" ", "_")
        
print(time.asctime())
#create the subdirectory if it isn't there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)
    
#we use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

#Run the backup
print('Zip command is: ')
print(zip_command)
print('Running...')
if os.system(zip_command) == 0:
    print('Successful backup to', target,'at ', time.asctime())
else:
    print('Backup FAILED')


