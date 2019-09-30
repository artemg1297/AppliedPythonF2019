import sys
import codecs
from class_outputjson import outputjson
from class_outputtsv import outputtsv
from class_helpfunc import helpfunc
from class_tryopen import tryopen

def trying(filename: str):
    st_code = ['utf8','utf16','cp1251']
    er = 0
    js = outputjson()
    ts = outputtsv()
    tr = tryopen()
    for i in range(len(st_code)):
        code = st_code[i]
        if tr.tryop(filename, code) == -1:
            print('Файл не валиден')
            return
        elif tr.tryop(filename, code) == 0:
            er = 1
        elif tr.tryop(filename, code) == 1:
            if tr.check(filename, code) == 'json':
                js.methout(filename, code)
                return
            elif tr.check(filename, code) == 'tsv':
                ts.methout(filename, code)
                return
    if er == 1:
        print('Формат не валиден')
    return

if __name__ == '__main__':
    filename = sys.argv[1]

trying(filename)
