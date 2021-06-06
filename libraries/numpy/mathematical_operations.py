import csv
import numpy as np


file_CSV = open('Edited_Earthquakes.csv')
data_CSV = csv.reader(file_CSV)
edited_earthquake = list(data_CSV)
edited_earthquake = np.array(edited_earthquake)
edited_earthquake = edited_earthquake.astype(np.float)
print(edited_earthquake)


print("Mean of first column: ", np.mean(edited_earthquake[:,0]) )
print("Mean of second column: ", np.mean(edited_earthquake[:,1]) )
print("Mean of third column: ", np.mean(edited_earthquake[:,2]) )
print("Mean of fourth column: ", np.mean(edited_earthquake[:,3]) )
print("Mean of fifth column: ", np.mean(edited_earthquake[:,4]) )



print("Standart deviation of first column: ", np.std(edited_earthquake[:,0]) )
print("Standart deviation of second column: ", np.std(edited_earthquake[:,1]) )
print("Standart deviation of third column: ", np.std(edited_earthquake[:,2]) )
print("Standart deviation of fourth column: ", np.std(edited_earthquake[:,3]) )
print("Standart deviation of fifth column: ", np.std(edited_earthquake[:,4]) )


subtract_to = [1,25,25,10,4]
print(edited_earthquake-subtract_to)



print(edited_earthquake*2)