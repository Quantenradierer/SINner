import random
from collections import defaultdict

REROLLS = 2
DICES = 5

SAMPLE_SIZE = 10000000


def roll():
    successes = 0
    for i in range(DICES):
        successes += random.randint(1, 3) == 3

    for _ in range(REROLLS):
        if successes < DICES:
            successes += random.randint(1, 3) == 3

    return successes


results = defaultdict(int)

for _ in range(SAMPLE_SIZE):
    successes = roll()
    results[successes] += 1

print("Erfolge:")
for key in sorted(results.keys()):
    print(key, "|", results[key] / SAMPLE_SIZE)
