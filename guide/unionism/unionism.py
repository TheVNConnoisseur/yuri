from os import makedirs, path
from yuri.fileformat import *
import yuri.yuridec as yuridec
import yuri.yuricom as yuricom
from multiprocessing import freeze_support

if __name__ == '__main__':
    freeze_support()

YPF_IN = '/tmp/unionism/game/pac/ysbin.ypf'
YPF_EX = '/tmp/unionism/extract_ypf'
YPF_VER = 500

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
DEC_YURI = '/tmp/unionism/decompile_yuri'
FORCE_VER = 480
YSTB_KEY = 0x9c28430c

if 0:
    yuridec.run(YBN_IN, DEC_YURI, key=YSTB_KEY, ver=FORCE_VER,
                dcls=yuridec.YDecYuri, also_dump=True)

COM_TEMP = '/tmp/unionism/com_work'
COM_OUT = '/tmp/unionism/output.ypf'
WRITE_VER = 554

if 1:
    yuricom.run(
        YSTB_KEY,
        DEC_YURI,
        FORCE_VER,
        COM_TEMP,
        YBN_IN,
        COM_OUT,
        t_ver=FORCE_VER,
        w_ver=WRITE_VER,
        ypf_ver=YPF_VER,
        # opts=yuricom.ComOpts(opt_v555_npar=False); # normal npar
    )
