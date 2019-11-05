# testing bayes classifiers
from bayes import *

dataset = [[3.393533211,2.331273381,0],
	[3.110073483,1.781539638,0],
	[1.343808831,3.368360954,0],
	[3.582294042,4.67917911,0],
	[2.280362439,2.866990263,0],
	[7.423436942,4.696522875,1],
	[5.745051997,3.533989803,1],
	[9.172168622,2.511101045,1],
	[7.792783481,3.424088941,1],
	[7.939820817,0.791637231,1]]

# Test separating data by class
print("# Test separating data by class")
separated = separate_by_class(dataset)
for label in separated:
	print(label)
	for row in separated[label]:
		print(row)


# Test summarizing a dataset
print("# Test summarizing a dataset")
summary = summarize_dataset(dataset)
print(summary)

# Test summarizing by class
print("# Test summarizing by class")
summary = summarize_by_class(dataset)
for label in summary:
	print(label)
	for row in summary[label]:
		print(row)


# Test Gaussian PDF
print("Step 4: Gaussian Probability Density Function")
print(calculate_probability(1.0, 1.0, 1.0))
print(calculate_probability(2.0, 1.0, 1.0))
print(calculate_probability(0.0, 1.0, 1.0))

#Class Probabilities
print("Step 5: Test Class Probabilities")
summaries = summarize_by_class(dataset)
probabilities = calculate_class_probabilities(summaries, dataset[0])
print(probabilities)