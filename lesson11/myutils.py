def printarr(a):
    for i in a:
        print(i)

def find_max(a):
    maxi = a[0]
    for i in a:
        if i>maxi:
            maxi = i
    return maxi
def find_real_age(d):
    return 2020-d['year']

def find_real_age1(year):
    return 2020-year


def some_find(d,key):
    return d[key]
