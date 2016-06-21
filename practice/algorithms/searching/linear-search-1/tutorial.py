def linearSearch():
    N,M = [int(x) for x in raw_input().split()]
    A = [int(x) for x in raw_input().split()]

    for i in xrange(N):
        if A[N - i - 1] == M:
            return N - i
    return -1

print(linearSearch())
