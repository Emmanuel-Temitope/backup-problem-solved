import os
import time

#The directory to backup.- Source Directory

source = [r'source']

'#Directory to store backup- Target Directory'
target_dir = r'target-directory'


'#compressed backup- Converted into a zip file.'
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S%p') + '.zip'


'#create a target directory if it is not present/valid'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(target, ''.join(source))

'#Run the backup'
print('Zip command is: ')
print(zip_command)
print('Running... ')
if os.system(zip_command) == 0:
    print('Successful backup to ', target)
else:
    print("BACKUP failed")
