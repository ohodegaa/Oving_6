__author__ = 'ohodegaa'


class test:
    def __init__(self):
        self.value = None

    def update(self, recommendation):
        self.value = recommendation

    def operationalize(self):
        for (func, args) in self.value:
            func(*args)

    def A(self):
        print("A: no args")

    def B(self, hello):
        print("B: 1 arg: ", hello)

    def C(self, a, b, c):
        print("C: 3 args: ", a, b, c)

    def main(self, t):
        self.update([(t.A, ()), (t.C, ("Halla balla", "hello", "hei"))])
        self.operationalize()


def find_index(liste):
    print((isinstance(x, test) for x in liste))


t = test()
liste = [t]
find_index(liste)
t.main(t)
