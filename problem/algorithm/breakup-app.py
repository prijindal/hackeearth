N = input()

counts = {}

for i in xrange(N):
    S = raw_input()
    weight = 0
    if S[0] == "G":
        weight = 2
    elif S[0] == "M":
        weight = 1
    numbers = [int(s) for s in S.split() if s.isdigit()]
    for i in numbers:
        if i not in counts:
            counts[i] = weight
        else:
            counts[i]+=weight

if len(counts) == 0:
    print("No Date")
else:
    m = max(counts, key=counts.get)
    if m == 19 or m == 20:
        print("Date")
    else:
        print("No Date")
