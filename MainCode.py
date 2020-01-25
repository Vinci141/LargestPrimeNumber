# Goal is to find largest prime number of a given number

def func1(num):
    i = 2
    pn = 1
    while num / i < num:
        if num % i == 0:
            pn = i
            num = num / i
            return pn
        else:
            i += 1

data = func1(19)
print(data)
