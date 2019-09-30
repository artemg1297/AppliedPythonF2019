import sys
import codecs
from class_outputjson import outputjson
from class_outputtsv import outputtsv
from class_helpfunc import helpfunc

def trying(filename: str):
    st_code = ['utf8','utf16','cp1251']
    er = 0
    js = outputjson()
    ts = outputtsv()
    for i in range(len(st_code)):
        code = st_code[i]
        if js.methout(filename, code) == 'Файл не валиден':
            print('Файл не валиден')
            return
        if ts.methout(filename, code) == 'Файл не валиден':
            print('Файл не валиден')
            return
        if js.methout(filename, code) == 1:
            return
        if ts.methout(filename, code) == 1:
            return
        if js.methout(filename, code) == 0:
            er = 1
        if ts.methout(filename, code) == 0:
            er = 1
    if er == 1:
        print('Формат не валиден')

if __name__ == '__main__':
    filename = sys.argv[1]

trying(filename)
