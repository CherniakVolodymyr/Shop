
d = [1]
def positive_sum(arr):
    num = arr
    nfor i in num:
        if i > 0:
            i += i
    return i
print(positive_sum(d))