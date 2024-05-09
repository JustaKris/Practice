# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrol_pumps):
    total_petrol = 0
    total_distance = 0
    start_index = 0
    tank = 0

    for i in range(len(petrol_pumps)):
        petrol, distance = petrol_pumps[i]
        total_petrol += petrol
        total_distance += distance
        tank += petrol - distance

        # If tank becomes negative, reset starting point and tank
        if tank < 0:
            start_index = i + 1
            tank = 0

    # If total petrol is less than total distance, no solution
    if total_petrol < total_distance:
        return -1
    else:
        return start_index


if __name__ == '__main__':
    n = int(input().strip())

    petrol_pumps = []

    for _ in range(n):
        petrol_pumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrol_pumps)
    print(result)


"""Sample Input 1
3
1 5
10 3
3 4
"""