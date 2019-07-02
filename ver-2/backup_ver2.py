# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 07:18:04 2019

@author: Emmanuel-Temitope
"""

import os
import time

#source directory for backup
#to be backup in a list , so can bakcup up multiple directories
#for names with spaces in it- ['"My Documents"']
source = ['"source"', r'another source']

target_dir = r'target'

#checking if the target-directory exists and creating it if not.
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#backup date
today = target_dir + os.sep + time.strftime('%Y%m%d')

#backup time
now = time.strftime('%H%M%S')

#target file to backup
target = today + os.sep + now + '.zip'

#check-2
if not os.path.exists(today):
    os.mkdir(today)
    
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))  

#Run the backup
print('The zip command is')
print(zip_command)
print('Running...')

if os.system(zip_command) == 0:
    print('Successful backup to ', target)
else:
    print('BACKUP FAILED')

#approximately 0.7milli-sec per 1mb
#and approximately 14.35mb per seconds
