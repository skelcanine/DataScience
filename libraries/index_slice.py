import csv
import numpy as np


file_CSV = open('Earthquakes.csv')
data_CSV = csv.reader(file_CSV)
earthquake_array = list(data_CSV)
earthquake_array = np.array(earthquake_array)
#print(earthquake_array)



edited_array = earthquake_array[0:20, :].copy()
#print(edited_array)
#print(edited_array[:, 4])
last_array = np.array([edited_array[:, 2].copy(),edited_array[:, 4].copy(),edited_array[:, 5].copy(),edited_array[:, 6].copy(),edited_array[:, 11].copy()])
last_array = last_array.astype(np.float).transpose()
last_arrayx = earthquake_array[:20,( 3,5,6,7,12)].copy()
last_arrayx = last_arrayx.astype(np.float)
print(last_arrayx)




print( np.where(last_arrayx[:,-1] > 4.5 )[0] )

last_arrayx[0,:]=1
print(last_arrayx)


np.savetxt('Edited_Earthquakes.csv',last_arrayx, delimiter=',')