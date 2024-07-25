from itertools import permutations

a = 'abc'
b = 'hjgcukyfaciyf'

perm = permutations(list(a))
lst = []

for i in perm:
    lst.append(''.join(i))

sol = False
for i in lst:
    if i in b:
        sol = True

print(sol)

# But this cause memory limit exceed error
# Bcz it takes O(n^2) Time complexity
