import csv

print("Importing CSV file...")

with open("data\Challenge_1_Training.csv", newline="") as csvfile:
	trainingCsvReader = csv.reader(csvfile, delimiter=",", quotechar="|")
	print("CSV file imported.")
	
	print("Converting CSV to list of lists...")
	trainingData = list(trainingCsvReader)
	trainingData = trainingData[1:51]
	print("Converted CSV to list of lists.")
	
	trainingOutputs = []
	print("Deleting inputs from output data...")
	for row in trainingData:
		trainingOutputs.append(row[49])
	
	trainingInputs = trainingData
	print("Deleting outputs from input data...")
	for row in trainingInputs:
		del row[49]
	
	
	while True:
		print("Input row:")
		row = int(input())
		
		print("Inputs:")
		print(trainingInputs[row])
		
		print("Output:")
		print(trainingOutputs[row])