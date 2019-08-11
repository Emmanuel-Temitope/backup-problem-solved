# backup-problem-solved
A python script that helps to backup easily offline.
It makes use of the zip command in archiving files into smaller bytes.
just strings might not work, so:
methods of adding of adding file directory
1. For name with spaces - e.g source = ['"source\\target Directory"']
2. For name with unicode error - e.g source = [r'target\directory']
This most times affect window users.

Examples for the sources and target-dir variables on windows
source = ['"C:\\Users\\Your Username\\sub-directory"', r'C:\Users\Your-Username\sub-directory']
target_dir = r'C:\Users\Your Username\Backup'

Format for both source and target_ on Linux and mac
target_dir = 'usr/dir/sub-directory'
