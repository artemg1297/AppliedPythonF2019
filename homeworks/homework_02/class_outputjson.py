import sys
import codecs
from class_helpfunc import helpfunc

class outputjson:

    def __int__(self):
        pass

    def methout(self, filename: str, code: str):
        cl = helpfunc()
        lidic = []
        d = {}
        ogl = ['Название','Ссылка','Теги','Оценка']
        maxlen = 0
        try:
            with codecs.open(filename, encoding = code) as fu:
                for line in fu:
                    st = line.strip().split(':')
        except FileNotFoundError:
            return 'Файл не валиден'
        except:
            return 0
        with codecs.open(filename, encoding = code) as fu:
            for line in fu:
                st = line.strip().split(':')
                for i in range(len(st)):
                    if len(st[i]) > maxlen:
                        maxlen = len(st[i])
                st[0] = st[0][1:-1]
                if st[0] in ogl:
                    d[st[0]] = ''
        minlen = 10
        totlen = 2*(maxlen + 5) + 2*minlen + 5*2 - 1
        k = -1
        with codecs.open(filename, encoding = code) as fu:
            for line in fu:
                st = line.strip().split(':')
                if '[' or '{' not in st:
                    st[0] = st[0][1:-1]
                    if st[0] == 'Название':
                        if k >= 0:
                            lidic.append(d)
                        k += 1
                        d = {}
                        st[1] = cl.delap(st[1])
                        d[st[0]] = st[1]
                    if st[0] == 'Ссылка':
                        st[1] = cl.delap(st[2])
                        d[st[0]] = st[1]
                    if st[0] == 'Теги':
                        st[1] = cl.delap(st[1])
                        d[st[0]] = st[1]
                    if st[0] == 'Оценка':
                        st[1] = cl.delap(st[1])
                        d[st[0]] = st[1]
            lidic.append(d)
        for i in range(len(lidic)):
            if type(lidic[i]) == 'str':
                continue
            else:
                if i == 0:
                    cl.sizeprint('^','-'*totlen, totlen, '', 0)
                    print()
                    for key in lidic[i].keys():
                        if key == 'Оценка' or key == 'Теги':
                            cl.sizeprint('^','| ', 1, key, minlen)
                        else:
                            cl.sizeprint('^','| ', 1, key, maxlen + 5)
                    print('|')
                for key in lidic[i].keys():
                    if key == 'Оценка':
                        cl.sizeprint('>','| ', 1, lidic[i][key], minlen)
                    elif key == 'Теги':
                        cl.sizeprint('<','| ', 1, lidic[i][key], minlen)
                    else:
                        cl.sizeprint('<','| ', 1, lidic[i][key], maxlen + 5)
                print('|')
        cl.sizeprint('^','-'*totlen, totlen, '', 0)
        return 1
