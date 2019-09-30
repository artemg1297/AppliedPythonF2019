import sys
import codecs
from class_helpfunc import helpfunc

class outputtsv:

    def __int__(self):
        pass

    def methout(self, filename: str, code: str):
        cl = helpfunc()
        maxlen = 0
        try:
            with codecs.open(filename, encoding = code) as fu:
                for line in fu:
                    line = line.strip()
        except FileNotFoundError:
            return 'Файл не валиден'
        except:
            return 0
        with codecs.open(filename, encoding = code) as fu:
            for line in fu:
                line = line.strip()
                st = line.split('\t')
                for i in range(len(st)):
                    if len(st[i]) > maxlen:
                        maxlen = len(st[i])
        minlen = 10
        totlen = 2*(maxlen + 5) + 2*minlen + 5*2 - 1
        with codecs.open(filename, encoding = code) as fu:
            for line in fu:
                line = line.strip()
                st = line.split('\t')
                title = st
                if st[0] == 'Название':
                    cl.sizeprint('^','-'*totlen, totlen, '', 0)
                    print()
                    for i in range(len(st)):
                        if st[i] == 'Оценка' or st[i] == 'Теги':
                            cl.sizeprint('^','| ', 1, st[i], minlen)
                        else:
                            cl.sizeprint('^','| ', 1, st[i], maxlen + 5)
                    print('|')

                else:
                    for i in range(len(st)):
                        if title[i] == 'Оценка':
                            cl.sizeprint('>','| ', 1, st[i], minlen)
                        elif title[i] == 'Теги':
                            cl.sizeprint('<','| ', 1, st[i], minlen)
                        else:
                            cl.sizeprint('<','| ', 1, st[i], maxlen + 5)
                    print('|')
            cl.sizeprint('^','-'*totlen, totlen, '', 0)
        return 1
