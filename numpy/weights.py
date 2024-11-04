import numpy as np

# Given the students' grades, we want to randomly select one based on the best grades by assigning weights to them
students = ['Joao', 'Marcos', 'Daniela', 'Pamela', 'Eva', 'Carlos']
grades   = np.array([40, 60, 50, 70, 90, 80])

print(grades)
# [40 60 50 70 90 80]

print(sum(grades))
# 390

probs = grades / sum(grades)
print(probs)
# Eva will have the greatest probability, followed by Carlos
# [0.1025641  0.15384615 0.12820513 0.17948718 0.23076923 0.20512821]

print(sum(probs))
# 1.0

print(np.random.choice(students, 1, p=probs))
# ['Eva']
