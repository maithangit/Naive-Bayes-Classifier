# method for reading dataset
import sys
from bayes import *
from csv import reader
from random import seed

print(sys.argv[1])

# dataset = [[3.393533211,2.331273381,0],
# 	[3.110073483,1.781539638,0],
# 	[1.343808831,3.368360954,0],
# 	[3.582294042,4.67917911,0],
# 	[2.280362439,2.866990263,0],
# 	[7.423436942,4.696522875,1],
# 	[5.745051997,3.533989803,1],
# 	[9.172168622,2.511101045,1],
# 	[7.792783481,3.424088941,1],
# 	[7.939820817,0.791637231,1]]

def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup

seed(1)
filename = 'datasets\\iris-flowers.csv'
dataset = load_csv(filename)

for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)