import sys
import codecs
from class_helpfunc import helpfunc


class outputtsv:

    def __int__(self):
        pass

    def methout(self, filename: str, code: str):
        cl = helpfunc()
        maxlen = 0
        with codecs.open(filename, encoding=code) as fu:
            for line in fu:
                line = line.strip()
                st = line.split('\t')
                for i in range(len(st)):
                    if len(st[i]) > maxlen:
                        maxlen = len(st[i])
        minlen = 12
        totlen = 2*(maxlen + 2) + 2*minlen + 3*1 - 1
        title = []
        with codecs.open(filename, encoding=code) as fu:
            for line in fu:
                line = line.strip()
                st = line.split('\t')
                if title == []:
                    title = st
                if st[0] == 'Название':
                    cl.sizeprint('^', '-'*totlen, totlen, '', 0)
                    print()
                    for i in range(len(st)):
                        if st[i] == 'Оценка' or st[i] == 'Теги':
                            cl.sizeprint('^', '|', 1, st[i], minlen)
                        elif st[i] == 'Ссылка':
                            cl.sizeprint('^', '|  ', 1, st[i], maxlen)
                        else:
                            cl.sizeprint('^','| ', 1, st[i], maxlen + 3)
                    print('|')
                else:
                    for i in range(len(st)):
                        if title[i] == 'Оценка':
                            cl.sizeprint('>', '|', 1, st[i], minlen - 2)
                        elif title[i] == 'Теги':
                            cl.sizeprint('<', '|  ', 1, st[i], minlen - 2)
                        elif title[i] == 'Ссылка':
                            cl.sizeprint('<', '|  ', 1, st[i], maxlen)
                        else:
                            cl.sizeprint('<', '|  ', 1, st[i], maxlen + 2)
                    print('  |')
            cl.sizeprint('^', '-'*totlen, totlen, '', 0)
        pass
