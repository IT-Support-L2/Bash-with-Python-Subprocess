#!/usr/bin/env python3
import sys
import subprocess
with open(sys.argv[1], 'r') as f:
    content1 = f.readlines()
    content2 = [x.strip() for x in content1]
    content3 = [item.replace("jane", "jdoe") for item in content2]
    res = dict(zip(content2, content3))
    for key, value in res.items():
        subprocess.run(['mv', '/home/ninja-coder/'+key, '/home/ninja-coder/'+value])