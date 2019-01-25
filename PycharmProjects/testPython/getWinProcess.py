# -*- coding:utf-8 -*-
import psutil
import re
import sys

def processInfo(x):
    p = psutil.get_process_list()
    for r in p:
        aa = str(r)
        f = re.compile(x,re.i)
        if f.search(aa):
            print aa.split('pid=')
processInfo(sys.argv[1])

