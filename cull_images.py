import os
from subprocess import Popen, PIPE
import re

# get available disk space from df
def get_avail():
    p = Popen(['df', '-B1', '/'], stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    out = [o for o in out.split('\n') if o != '']
    df = {k:v for k,v in zip(*[re.split('\s+', o) for o in out])}
    return int(df['Available'])

avail = get_avail()
min_avail = 2**20 * 100
dir = '/motion/'

if avail < min_avail:
    print 'Available space {} is less than minimum ({})'.format(avail, min_avail)

    files = [
        (dir+f, os.stat(dir+f).st_ctime, os.path.getsize(dir+f))
        for f in [w for w in os.walk(dir)][0][2]
        ]
    files.sort(key=lambda x: x[1])

    rm_files = []
    size_of_rm_files = 0
    for f in files:
        if avail + size_of_rm_files > min_avail:
            break
        else:
            rm_files.append(f[0])
            size_of_rm_files += f[2]

    for f in rm_files:
        print ' removing {}'.format(f)
        os.remove(f)
    print 'Available space is now {}'.format(get_avail())
else:
    print 'Available space {} exceeds minimum ({})'.format(avail, min_avail)
