def checkPalindrome(N):
    A = str(N)
    l = len(A)
    for i in xrange(0, l):
        if A[i] != A[l - i - 1]:
            return False
    return True

def checkMirrors(N):
    for i in str(N):
        if i not in ['0','1','8']:
            return False
    return True

for i in xrange(input()):
    N = raw_input()
    if checkPalindrome(N) == False:
        print("NO")
    elif checkMirrors(N) == False:
        print("NO")
    else:
        print("YES")
