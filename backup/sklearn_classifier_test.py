from sklearn import tree

#Training Input Data
print("Importing training input data...")
x = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

#Training Output Data
print("Importing training output data...")
y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

#Training
print("Creating classifier...")
classifier = tree.DecisionTreeClassifier()

print("Training model...")
classifier = classifier.fit(x, y)
print("Model trained.")

#Predicting
print("Input your data to predict the output.")
prediction = classifier.predict([[190, 70, 43]])
print("Predicted output:")
print(prediction)