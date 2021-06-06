import numpy as np

firstfeature = [50,60,70,90,100,120,150,180,200,250]
secondfeature = [1,2,3,4,5,6,7,8,9,10]
thirdfeature = [30000,45000,55000,70000,80000,100000,150000,200000,230000,300000]
all_features = np.array(firstfeature+secondfeature+thirdfeature)
print(all_features)

transposed_array = all_features.transpose()
print(transposed_array)

print(transposed_array.shape)
print("This is 1d array with 30 rows")

# function that returns an array of ones with zeros where both row and column numbers are even.

def funcx(a, b):
  array = np.full((a,b),1)
  for x in range(a):
    for y in range(b):
      if((x%2 & y%2) == 1):
        array[x][y]=0
  return array

rcount = input("Enter row count: ")
ccount = input("Enter column count: ")

print(funcx(int(rcount),int(ccount)))