"""
lib_ozy.py
"""

import time
import os
from pathlib import Path

import time
from datetime import datetime as dt
from colorama import Fore, Back, init
# import art

init()
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


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


    def logTime(self, label='', sep='',**kwargs):
        # dest_ex = os.path.isfile(pdest)
        # if not os.path.isfile(fn): return False
        # shutil.copy(pfrom, pdest)
        start=''
        end=''

        # label color
        start_colr=''
        end_colr=''
        if 'start' in kwargs:
            start = kwargs['start']
        if 'end' in kwargs:
            end = kwargs['end']
        # if start and not end :
        #     end = kwargs['end']
        if 'start_colr' in kwargs:
            start_colr = kwargs['start_colr']
        if 'end_colr' in kwargs:
            end_colr = kwargs['end_colr']
        if start_colr and not end_colr :
            end_colr = color.END
        # print(color.BOLD+color.BLUE+'========== =========='+color.END)
        if start_colr :
            label = start_colr+label
        if end_colr :
            label = label+end_colr
        
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