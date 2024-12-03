"""
Los Historiadores Senior Elfos tienen un problema: su lista de ubicaciones está vacía.

Comienzan con la oficina del Historiador Jefe, donde encuentran notas y listas de ubicaciones significativas.

Estas notas podrían ayudar a determinar qué ubicaciones buscar.
"""


""""
So we have a 2 lists of numbers.

1/ Need to rank each list from smallest to largest.
2/ Then pair up the numbers
3/ measure how far apart they are.
4/ Add up all the distances.

For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

"""

# 1 Convert the .txt file into 2 lists of numbers (CSV)

list1 = []
list2 = []

with open('uno/input.txt') as f:
    for line in f:
        list1.append(int(line.split('   ')[0]))
        list2.append(int(line.split('   ')[1]))


# 2 Rank each list from smallest to largest

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# print("Sorted List 1:", sorted_list1[0:8])
# print("Sorted List 2:", sorted_list2[0:8])

# 3 Pair up the numbers

# print(len(sorted_list1))
# print(len(sorted_list2))

# 4 Measure how far apart they are

pairs = []

for i in range(len(sorted_list1)):
    pairs.append((sorted_list1[i], sorted_list2[i]))

# print(pairs[:8])

# 5 Add up all the distances

for i in range(len(pairs)):
    distance = abs(pairs[i][0] - pairs[i][1])
    print(distance)

total_distance = sum([abs(pair[0] - pair[1]) for pair in pairs])
print(f"Total distance: {total_distance}")