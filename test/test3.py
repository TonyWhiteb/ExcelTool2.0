import pysnooper


def average(number):
    s = 0
    for i in range(1, number + 1):
        s += i

    with pysnooper.snoop():
        avg = s / number

        return avg


print(average(5))