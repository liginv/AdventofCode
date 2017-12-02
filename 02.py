from sys import argv


def split_row():
    script, filename = argv
    text = open(filename, 'r')
    file = text.read()
    text.close()

    # spliting into each row
    ip = file.strip()
    ip = ip.split('\n')

    # spliting each element in a row
    new_list = []
    for i in ip:
        s = i.split(' ')
        new_list.append(s)

    # convert elements from str to int
    num_list = []
    for i in new_list:
        temp = []
        for j in i:
            num = int(j)
            temp.append(num)
        num_list.append(temp)

    return num_list


input_list = split_row()

# sorting each elements in the list of lists
calc_list = []
for i in input_list:
    calc_list.append(sorted(i))

big_list = []
small_list = []

# Biggest element in each row
for i in calc_list:
    big_list.append(i[-1])

# Smallest element in each row
for i in calc_list:
    small_list.append(i[0])

# Finding  the difference between big & small
diff_list = []

for i in range(len(big_list)):
    diff_list.append(big_list[i] - small_list[i])

sum = 0

for i in range(len(diff_list)):
    sum += diff_list[i]

print(sum)
