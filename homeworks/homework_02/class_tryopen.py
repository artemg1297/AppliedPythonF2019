class tryopen:

    def __int__(self):
        pass

    def tryop(self, filename: str, code: str):
        try:
            with open(filename, encoding=code) as fu:
                st = fu.readline()
        except FileNotFoundError:
            return -1
        except:
            return 0
        else:
            return 1

    def check(self, filename: str, code: str):
        with open(filename, encoding=code) as fu:
            st = fu.readline()
            if '[' in st:
                return 'json'
            else:
                return 'tsv'
