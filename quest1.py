import string
import numpy as np
import re

def find_sos(array):
    sentence = "".join(array)
    return len(re.findall('(?=SOS)', sentence))

array = np.random.choice(list(('S', 'O')),  size=(10,10))

for i in range (10):
    for j in range(10):
        print(array[i][j], end = " ")
    print()
    
reversed_array = array[...,::-1]
column_count = 0
for i in range(10):
    column_count += find_sos(array[:,i])

row_count = 0
for i in range(10):
    row_count += find_sos(array[i])

diagonal_count = 0
for i in range(10-2):
    if i == 0:
        diagonal_count += find_sos(np.diag(array, i))
        continue
    diagonal_count += find_sos(np.diag(array, i))
    diagonal_count += find_sos(np.diag(array, -i))

reversed_diagonal_count = 0
for i in range(10-2):
    if i == 0:
        reversed_diagonal_count += find_sos(np.diag(reversed_array, i))
        continue
    reversed_diagonal_count += find_sos(np.diag(reversed_array, i))
    reversed_diagonal_count += find_sos(np.diag(reversed_array, -i))

print("total column sos: ", column_count)
print("total row sos: ", row_count)
print("total diagonal sos: ", diagonal_count)
print("total reversed diagonal sos: ", reversed_diagonal_count)
