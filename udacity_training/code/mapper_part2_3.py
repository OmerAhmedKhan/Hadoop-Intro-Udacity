#!/usr/bin/python

# Format of each line is:

import sys

for line in sys.stdin:
    data = line.replace('"', '').strip().split(" ") #Line split on simple space
    if len(data) == 10:
        ip, time, c_id, c_uname, time, request_type, files, http, status, bytes  = data
    print files.replace('http://www.the-associates.co.uk', '')

