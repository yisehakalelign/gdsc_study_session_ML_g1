# import numpy liberary
import numpy as np
#1.crate a list of five numbers
numbers_list = [98, 89, 95, 85, 90]
#2.convert the list in to a numpy array
numbers_array = np.array(numbers_list)
#3.calculate the mean, maximum value and sum
mean_value = np.mean(numbers_array)  # calculate the mean value of the list which is the avarage
max_value = np.max(numbers_array)  # tells us the maximum nuber from the list
sum_value = np.sum(numbers_array)  # calculates the thed sum of the list
#4.print the result clrearly
print("original list:", numbers_list)
print("numpy array:", numbers_array)
print("mean_value:", mean_value)
print("maximum value:", max_value)
print("sum value:", sum_value)