lst = []

def foo1(bar=lst):
    bar.append(1)
    print(bar)

foo1()
foo1()
foo1()


def foo2(bar):
    bar.append(1)
    print(bar)

foo2(lst)
foo2(lst)
foo2(lst)
