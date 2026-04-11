from os import makedirs, path
from yuri.fileformat import *
import yuri.yuridec as yuridec
import yuri.yuricom as yuricom
from multiprocessing import freeze_support

# Windows need this for multiprocessing
if __name__ == '__main__':
    freeze_support()

# change to your own path
YPF_IN = '/tmp/fraternite/game/pac/bn.ypf'
YPF_EX = '/tmp/fraternite/extract_ypf'
YPF_VER = 490  # change this to your value

if 0:
    # YPF_IN: input ypf file
    # YPF_EX: folder to extract into
    with open(YPF_IN, 'rb') as fp:
        # ents: entries in ypf
        # ver: ypf version
        ents, ver = ypf_read(fp)
        print('ypf ver', ver)
    # name: file name (e.g. "ysbin\yst00001.ybn")
    # k: file kind
    # c: compression (0 - none, 1 - deflate)
    # data: file data, decompressed
    # ul: uncompressed length
    for name, k, c, data, ul in ents:
        print('file', name, k, c, ul)
        out_name = path.join(YPF_EX, *name.split('\\'))
        makedirs(path.dirname(out_name), exist_ok=True)
        with open(out_name, 'wb') as fp:
            fp.write(data)

YBN_IN = path.join(YPF_EX, 'ysbin')
DEC_OUT = '/tmp/fraternite/decompile_yst'
FORCE_VER = 480  # force version 480
YSTB_KEY = 0x76033b26
DEC_YURI = '/tmp/fraternite/decompile_yuri'

if 0:
    # parameter 0: input folder, it should contain your ybn files directly
    # parameter 1: output folder, to which the decompiler will create files
    # yuridec.run(YBN_IN, DEC_OUT)
    # keyword argument "ver", force version
    # yuridec.run(YBN_IN, DEC_OUT, ver=FORCE_VER)
    # keyword argument "key", YSTB decryption key
    # yuridec.run(YBN_IN, DEC_OUT, ver=FORCE_VER, key=YSTB_KEY)
    # use YURI format for compiling
    yuridec.run(YBN_IN, DEC_YURI, ver=FORCE_VER, key=YSTB_KEY, dcls=yuridec.YDecYuri, also_dump=True)
    # If you have official YSCom.ycd
    # with open('YSCom.ycd', 'rb') as fp:
    #     yscd = YSCD.read(Rdr.from_bio(fp))
    # yuridec.run(YBN_IN, DEC_OUT, ver=FORCE_VER, key=YSTB_KEY, yscd=yscd)

COM_TEMP = '/tmp/fraternite/com_work'
COM_OUT = '/tmp/fraternite/output.ypf'
WRITE_VER = 490

if 1:
    yuricom.run(
        YSTB_KEY,  # [0]: YSTB key
        DEC_YURI,  # [1]: input source files
        FORCE_VER,  # [2]: (real) version of files
        COM_TEMP,  # [3]: temporary directory for the compiler
        YBN_IN,  # [4]: for some original ybn files from the game
        COM_OUT,  # [5]: output ysbin.ypf
        t_ver=FORCE_VER,  # keyword: if you forced version, also pass this for game original files
        w_ver=WRITE_VER,  # keyword: the version number the game used
        ypf_ver=YPF_VER,  # keyword, the version number the game used for YPF
    )
