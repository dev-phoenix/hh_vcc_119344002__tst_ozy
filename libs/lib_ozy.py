"""
lib_ozy.py
"""

import time
import os
from pathlib import Path

import time
from datetime import datetime as dt


def _print(*args, **kwargs):
    print(*args, **kwargs)


class POLog():
    '''
    Parser Ozon Log Controller
    '''
    logPath='./log/log.txt'
    logName='log.txt'
    print=False
    savelog = False
    prefix = ''
    def __init__(self, prefix=''):
        pdest = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'/_log/'
        dest_ex = os.path.isdir(pdest)
        if not dest_ex:Path('_log').mkdir()
        self.logPath = pdest+self.logName
        self.print=True
        self.savelog=True
        self.prefix=prefix

        self.end()
        dttpl = 'Started at: {} {}'
        st = dttpl.format(dt.now().ctime(), ('('+self.prefix+')') if self.prefix else '' )
        print(st)
        self.tmlog = time.time()
        self.save(st)


    def logTime(self, label='', sep=''):
        # dest_ex = os.path.isfile(pdest)
        # if not os.path.isfile(fn): return False
        # shutil.copy(pfrom, pdest)
        self.tlog(label, sep)


    def copy(self):
        # dest_ex = os.path.isfile(pdest)
        # if not os.path.isfile(fn): return False
        # shutil.copy(pfrom, pdest)
        ...

    
    def save(self,st=''):
        with open(self.logPath, 'a') as hendl:
            st += "\n"
            hendl.write(st);


    def tlog(self, label='', sep=''):
        if not self.savelog: return
        if len(sep): print(sep)
        label = self.prefix+label
        ct = time.time()
        betw = ct - self.tmlog
        h = betw//3600
        bt = betw-(h*3600)
        m = bt//60
        s = int(bt-(m*60))
        ms = int((bt-int(bt))*10000)
        tpl='{0:02d}h {1:02d}m {2:02d}s .{3:04d}ms {4}'
        # args = ('Time forced:',tpl.format(int(h),int(m),s, ms, ('('+label+')') if label else '' ))
        args = ('Time spent:',tpl.format(int(h),int(m),s, ms, ('('+label+')') if label else '' ))
        print(*args)
        self.save(' '.join(args))
    

    def end(self):
        self.save()