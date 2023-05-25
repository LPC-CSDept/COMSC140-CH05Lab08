def myfunc(lst):
    print(id(lst), 'ID of lst in myfunc() as soon as the function starts')
    lst[0] = 999
    print(id(lst), 'ID of lst in myfunc() after changing value of the 1st element')
    return lst


def main():
    numbers = [1, 2, 3]
    print(id(numbers), 'numbers ID ')

    # retlst = myfunc(numbers)
    a, *retlst = myfunc(numbers)

    retlst[0] = 999
    print(id(retlst), 'retlst ID: returned from myfunc')

    print(numbers)
    print(retlst)


if __name__ == '__main__':
    main()
