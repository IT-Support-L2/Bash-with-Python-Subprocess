#!/usr/bin/env python3
import sys
import subprocess
with open(sys.argv[1], 'r') as f:
    content1 = f.readlines()
    content2 = [x.strip() for x in content1]
    content3 = [item.replace("jane", "jdoe") for item in content2]
    res = dict(zip(content2, content3))
    for key, value in res.items():
        subprocess.run(['mv', '/directory/'+key, '/directory/'+value])
        
<<COMMENTS
This Python script reads sys.avg[1] or the argument == file which will be executed with it. On Linux OS, command to run is  ./changeName.py matched_pattern.txt
The use of subprocess module is a must since it's requested in the mentioned assessment. Subprocess will run bash command.
Finally, this script will substitute the old files usernames with the new ones after searching for it in the given directory.
The hard part is that the pattern must match a part of the file name and change it. As an example of a file name to change: dxc98jane_rpt.doc >> dxc98jdoe_rpt.doc
COMMENTS
