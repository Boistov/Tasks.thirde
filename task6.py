d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
l1 = ['A', 'C', 'F']

new_dict = {}

for key in d1:
    if key in l1:
        new_dict[key] = d1[key]

print(new_dict)
