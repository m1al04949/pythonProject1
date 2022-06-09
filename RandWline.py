import string

str = ''
strout = ''
raz = ''
count = 0

lst_1 = [x for x in range(1,27)]
lst_2 = list(string.ascii_lowercase)
lst_3 = list(string.ascii_uppercase)
dict1 = dict(zip(lst_1, lst_2))
dict2 = dict(zip(lst_1, lst_3))

with open('C:/Users/gorbunovia/Downloads/dataset_3363_2.txt', 'r') as line:
    str = line.readline()

for i in str:
    count += 1
    if (i in dict1.values() or i in dict2.values()) and raz != '':
        strout += symbol * int(raz)
        raz = ''
    if i in dict1.values() or i in dict2.values():
        symbol = i
    else:
        raz += i
    if count == len(str):
        strout += symbol * int(raz)

with open('C:/Users/gorbunovia/Downloads/dataset_3363_2.txt', 'w') as line:
    line.write(strout)

print(str)
print(strout)






