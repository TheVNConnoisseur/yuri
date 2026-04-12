from os import makedirs, path
from yuri.fileformat import *
import yuri.yuridec as yuridec
import yuri.yuricom as yuricom
from multiprocessing import freeze_support

# Windows need this for multiprocessing
if __name__ == '__main__':
    freeze_support()

YPF_IN = '/tmp/fraternite_hd/game/pac/bn.ypf'
YPF_EX = '/tmp/fraternite_hd/extract_ypf'
YPF_VER = 490

if 0:
    with open(YPF_IN, 'rb') as fp:
        ents, ver = ypf_read(fp)
        print('ypf ver', ver)
    for name, k, c, data, ul in ents:
        print('file', name, k, c, ul)
        out_name = path.join(YPF_EX, *name.split('\\'))
        makedirs(path.dirname(out_name), exist_ok=True)
        with open(out_name, 'wb') as fp:
            fp.write(data)

YBN_IN = path.join(YPF_EX, 'ysbin')
DEC_YURI = '/tmp/fraternite_hd/decompile_yuri'
VERSION = 481  # no need to force, it's really 481
YSTB_KEY = 0x37dfa895

if 0:
    yuridec.run(YBN_IN, DEC_YURI, key=YSTB_KEY, dcls=yuridec.YDecYuri, also_dump=True)


COM_TEMP = '/tmp/fraternite_hd/com_work'
COM_OUT = '/tmp/fraternite_hd/output.ypf'

if 1:
    yuricom.run(
        YSTB_KEY,
        DEC_YURI,
        VERSION,
        COM_TEMP,
        YBN_IN,
        COM_OUT,
        # t_ver=VERSION,  # no need for this
        # w_ver=VERSION,  # no need for this
        ypf_ver=YPF_VER,  # YPF version is 490
        opts=yuricom.ComOpts(opt_v555_npar=True)
    )
