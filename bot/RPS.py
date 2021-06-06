import random
# 1= rock
# 2 = paper
# 3 = scissor


def rps(a):
    b = random.randrange(1, 4)
    if a == b:
        return 0
    elif a == 1 and b == 2:
        return -1
    elif a == 2 and b == 1:
        return 1
    elif a == 1 and b == 3:
        return 1
    elif a == 3 and b == 1:
        return -1
    elif a == 3 and b == 2:
        return 1
    elif a == 2 and b == 3:
        return -1

# for i in range(1,30):
#     print(random.randrange(1,4))

for i in range(1,20):
    print(rps(2))  
    
    
