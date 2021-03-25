import csv
import numpy as np


file_CSV = open('x.csv')
data_CSV = csv.reader(file_CSV)
earthquake_array = list(data_CSV)
earthquake_array = np.array(earthquake_array)
earthquake_array = earthquake_array.astype(np.float)
print(earthquake_array)