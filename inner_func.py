def double_deker():
    print("starting double deker")
    def inner_fun():
        print("inner function start")
        return 3000
    
    return inner_fun
    

# print(double_deker())
# print(double_deker()())


def do_something(work):
    print("work starting..")
    # print(work)
    work()
    print("work ending")

# do_something(5)
# do_something("katai lekche")
def coding():
    print("learning python")
do_something(coding)