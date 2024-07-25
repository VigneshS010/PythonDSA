N = 3
coins = [1,2,3]
freq = [1,1,3]
V = 6

for i in range(len(coins)):
    for j in range(len(freq)):
        if coins[i] + freq [j] == V:
            print(str(coins[i]) +" "+ str(freq [j]))
