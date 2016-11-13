import csv
from sklearn import tree

#Import training data CSV
print("Importing CSV file...")
with open("data\Challenge_1_Training.csv", newline="") as csvfile:
	trainingCsvReader = csv.reader(csvfile, delimiter=",", quotechar="|")
	print("CSV file imported.")
	
	#Convert CSV reader object to list of lists
	print("Converting CSV to list of lists...")
	trainingData = list(trainingCsvReader)
	trainingData = trainingData[1:51]
	print("Converted CSV to list of lists.")
	
	#Training output data
	trainingOutputs = []
	print("Deleting inputs from output data...")
	for row in trainingData:
		trainingOutputs.append(row[49])
	
	#Training input data
	trainingInputs = trainingData
	print("Deleting outputs from input data...")
	for row in trainingInputs:
		del row[49]

#Training
print("Creating classifier...")
classifier = tree.DecisionTreeClassifier()

print("Training model...")
classifier = classifier.fit(trainingInputs, trainingOutputs)
print("Model trained.")

#Predicting
print("Input your data to predict the output.")
prediction = classifier.predict([['22915332', '1475073', 'Caucasian', 'Female', '[80-90)', '?', '3', '1', '4', '5', 'MC', '?', '79', '1', '25', '3', '0', '0', '518', '428', '496', '9', 'None', 'None', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Steady', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes']])
print("Predicted output:")
print(prediction)