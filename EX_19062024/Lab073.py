def outer_fun():
    a=30
    def inner_fun():
        print(a)
    inner_fun()
outer_fun()