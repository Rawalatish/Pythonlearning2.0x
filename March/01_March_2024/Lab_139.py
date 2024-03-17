# Till now we discussed ==> Core Programming + OOPs + Exceptions

def f1():
    print("f1")


def f2():
    print("f2")


def f3():
    print("f3")


def main():
    f1()
    print("main")


if __name__ == "__main__":                           # in main method defined sequence is followed
                                                     # main method madhye ji method pahila lihato ti pahila call hote
    main()
    # f1()
    # f2()