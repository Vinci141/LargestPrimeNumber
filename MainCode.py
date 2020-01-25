# Goal is to find largest prime number

def FindLargestPrimeNumber (input):
    min_value = 2
    prime_num = 1
    while input / min_value < input:
        if input % min_value == 0:
            prime_num = min_value
            input = input / min_value
            return prime_num
        else:
            min_value += 1


data = FindLargestPrimeNumber(21)
print(data)
