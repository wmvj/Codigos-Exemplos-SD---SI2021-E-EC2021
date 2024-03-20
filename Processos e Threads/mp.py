from multiprocessing import Process
from time import *
from random import *


def sleeper(name):
    t = gmtime()
    s = randint(1, 20)
    txt = str(t.tm_min)+':'+str(t.tm_sec)+' '+name + \
        ' vai dormir por '+str(s)+' segundos'
    print(txt)
    sleep(s)
    t = gmtime()
    txt = str(t.tm_min)+':'+str(t.tm_sec)+' '+name+' acordou'
    print(txt)


if __name__ == '__main__':
    p = Process(target=sleeper, args=('eve',))
    q = Process(target=sleeper, args=('bob',))
    p.start()
    q.start()
    p.join()
    q.join()
