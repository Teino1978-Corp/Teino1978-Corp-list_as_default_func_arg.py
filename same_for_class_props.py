class Foo:
    bar = []

ham = Foo()
spam = Foo()

ham.bar.append(1)
print(spam.bar)
