for i in xrange(input()):
    N = input()
    if N%21 == 0:
        print("The streak is broken!")
    elif str(N).find('21') >=0:
        print("The streak is broken!")
    else:
        print("The streak lives still in our heart!")
