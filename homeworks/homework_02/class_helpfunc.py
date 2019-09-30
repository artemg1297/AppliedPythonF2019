class helpfunc:

    def __int__(self):
        pass

    def define(self, filename: str):
        if 'utf8' in filename:
            code = 'utf8'
        elif 'utf16' in filename:
            code = 'utf16'
        elif 'cp1251' in filename:
                code = 'cp1251'
        else:
            code = None
        lis = filename.split('.')
        if lis[1] == 'json' or lis[1] == 'tsv':
            tipe = lis[1]
        else:
            tipe = None
        return code, tipe

    def delap(self, st: str):
        if '//' in st:
            st = '"https:' + st
        st = st.strip()
        if not(st > '0' and st < '9'):
            st = st[1:-2]
        return st

    def sizeprint(self, str0: str, st1: str, k1: int, st2: str, k2: int):
        fr1 = '{:^' + str(k1) + '}'
        fr2 = '{:' + str0 + str(k2) + '}'
        print(fr1.format(st1), end = '')
        print(fr2.format(st2), end = '')
