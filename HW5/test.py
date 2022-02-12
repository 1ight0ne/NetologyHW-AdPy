from datetime import datetime

def foo():
    print("вызвана функция foo")


def foo2():
    print("start")
    foo()
    print("end")


x = foo2
# x()

# ---------------------------------------

def start_end_patcher(old_fun):

    def new_fun():
        print("start new_fun")
        result = old_fun()
        print("end")
        return result

    return new_fun

foo = start_end_patcher(foo) #@start_end_patcher

# foo()

