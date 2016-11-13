import csv

print("Importing CSV file...")

with open("data\Challenge_1_Training.csv", newline="") as csvfile:
	trainingCsvReader = csv.reader(csvfile, delimiter=",", quotechar="|")
	print("CSV file imported.")
	
	print("Converting CSV to list of lists...")
	trainingData = list(trainingCsvReader)
	trainingData = trainingData[1:]
	print("Converted CSV to list of lists.")
	
	a = input()
	
	print("Each row:")
	for row in trainingData:
		a = input()
		print(", ".join(row))