# -*- coding:utf-8 -*-
import psutil
import re
import sys

def processInfo(x):
    p = list(psutil.process_iter())
    print(p)
    for r in p:
        aa = str(r)
        f = re.compile(x, re.I)
        if f.search(aa):
            print(aa.split('pid='))

processInfo(sys.argv[0])



