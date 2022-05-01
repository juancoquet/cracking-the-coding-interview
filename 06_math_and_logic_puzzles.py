import random

# 6.7 the apocalypse
def simulate_births(n=1000):
    # 0 = boy, 1 = girl
    births = []
    for _ in range(n):
        while birth := random.randint(0, 1) != 1:
            births.append(birth)
        births.append(birth)
    return sum(births) / len(births)