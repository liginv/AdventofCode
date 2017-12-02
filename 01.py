from sys import argv


def split_each_char():
    # getting the file from the user
    script, filename = argv
    text = open(filename, 'r')
    file = text.read()
    text.close()

    # spliting each char
    input = file.replace("", " ")[1: -1]
    input = input.split(' ')

    # making all the elements to int
    input = list(map(int, input))

    return input

#  ---PART ONE ---
print("---PART ONE ---")
ip = split_each_char()
sum = 0
new_list = []

for i, j in zip(ip, ip[1:]+[ip[0]]):
    if i == j:
        new_list.append(i)

for i in new_list:
    sum += i

print(sum)

#  --PART TWO ---
print("---PART ONE ---")
t1 = ip[:len(ip)//2]
t2 = ip[len(ip)//2:]
sum = 0
new_list = []

for i, j in zip(t1, t2):
    if i == j:
        new_list.append(i)
        new_list.append(j)
for i in new_list:
    sum += i

print(sum)
