def binarySearch(A, value):
    pass
    high = len(A) - 1
    low = 0
    while low <= high:
        mid = (low + high) / 2
        if A[mid] < value:
            low = mid + 1
        elif A[mid] > value:
            high = mid
        else:
            return mid + 1
    return -1

def binarySearchHelper(N, A, q):
    if A[0] > A[1]:
        A.reverse()
    x = [input() for x in xrange(q)]
    for i in x:
        print(binarySearch(A, i))

binarySearchHelper(
    input(),
    [int(x) for x in raw_input().split()],
    input()
    )
