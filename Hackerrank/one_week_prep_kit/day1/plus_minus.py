#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    ratios = {
        "pos": len([num for num in arr if num > 0]),
        "neg": len([num for num in arr if num < 0]),
        "zero": len([num for num in arr if num == 0])
    }

    for ration in ratios.values():
        print(f"{ration / len(arr):.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


'''Test Input
6
-4 3 -9 0 4 1
'''
