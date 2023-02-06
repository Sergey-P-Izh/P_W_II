coins = [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0]
print(coins.count(0) if coins.count(0) < coins.count(1) else coins.count(1))
