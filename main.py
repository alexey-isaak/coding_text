#str_first = input("Введите строку символов:")
from itertools import count
from collections import Counter

str_first = 'aaaaaaaaagggggrrrrrrryyxbttttttttuuuuuuppppppp'

print(str_first)

A = []
c_char = 0
i = 0
for i in range(len(str_first)):
    if i == len(str_first) - 1:
        A.append(str_first)

    elif str_first[i] == str_first[i + 1]:
        c_char = c_char + 1

    else:
        c_char = c_char + 1
        A.append(str_first[:c_char])
#print(A)

B = []
B.append(A[0])

for j in range(1, len(A)):
    B.append(A[j][(len(A[j - 1])):])

#print(B)
C = []

for i in range(len(B)):
    C.append(B[i][0])
    if len(B[i]) != 1:
        C.append(len(B[i]))

str_C = ''.join(map(str, C))
print(str_C)