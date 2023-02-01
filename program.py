import time
import random
import matplotlib.pyplot as plt

start_time = time.time()

people = []
for i in range(0, 50):
    people.append(100)

for beshkan in range(0, 10000):
    for person1 in range(0, 50):
        if (people[person1] == 0):
            continue
        person2 = 0
        while person2 == 0:
            person2 = random.randrange(0, len(people))

        people[person1] -= 1
        people[person2] += 1

print(people)
people.sort()
# Create bars
plt.bar(range(0,50), people)

# Create names on the x-axis
plt.xticks(range(0,50), range(0,50))

# Show graphic
plt.show()

# print("Process finished --- %s seconds ---" % (time.time() - start_time))
