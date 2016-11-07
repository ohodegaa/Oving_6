__author__ = 'ohodegaa'


class noe_rart:
    def __init__(self):
        self.value = None

    def update(self, recommendation):
        self.value = recommendation

    def operationalize(self):
        for (func, args) in self.value:
            print(*args)
            func(*args)

    def A(self):
        print("A: no args")

    def B(self, hello):
        print("B: 1 arg: ", hello)

    def C(self, a, b, c):
        print("C: 3 args: ", a, b, c)

    def main(self, t):
        self.update([(t.B, ["hello"]), (t.C, ("Halla balla", "hello", "hei"))])
        self.operationalize()


def find_index(liste):
    print((isinstance(x, noe_rart) for x in liste))


t = noe_rart()
liste = [t]
find_index(liste)
t.main(t)
