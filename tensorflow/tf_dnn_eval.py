#This code was heavily based on several tutorials from tensorflow.org.
#Many parts were combined, excluded, and modified to create a DNN model specific to this problem.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import tensorflow as tf
import pandas as pd
import numpy as np

def makeitglobal():
    global input_list

makeitglobal()

input_list = sys.argv
print(input_list)

del input_list[0]
input_list.insert(0, 1)
input_list.insert(0, 1)
input_list.append("<30")

if len(input_list) != 50:
    raise Exception("xxxxxxxxxxIncorrect number of arguments!")

try:
    input_list[4] = input_list[4] + ")"
    input_list[6] = int(input_list[6])
    input_list[7] = int(input_list[7])
    input_list[8] = int(input_list[8])
    input_list[9] = int(input_list[9])

    input_list[12] = int(input_list[12])
    input_list[13] = int(input_list[13])
    input_list[14] = int(input_list[14])
    input_list[15] = int(input_list[15])
    input_list[16] = int(input_list[16])
    input_list[17] = int(input_list[17])


    input_list[18] = str(input_list[18])
    input_list[19] = str(input_list[19])
    input_list[20] = str(input_list[20])

    input_list[21] = int(input_list[21])

except:
    raise Exception("xxxxxxxxxxCannot format inputs!")




print(input_list)
print(input_list[0])
print(input_list[1])
print(input_list[2])
print(input_list[3])
print(input_list[4])
print(input_list[5])
print("Formatted list:")
print(input_list)



print(input_list)
print("yolo")

tf.logging.set_verbosity(tf.logging.INFO)

flags = tf.app.flags
FLAGS = flags.FLAGS

#Define flags (variables for training)
flags.DEFINE_string("model_dir", "", "Base directory for output models.")
flags.DEFINE_string("model_type", "deep", "Valid model types: {'wide', 'deep', 'wide_n_deep'}.")
flags.DEFINE_integer("train_steps", 10, "Number of training steps.")
flags.DEFINE_string("train_data", "", "Path to the training data.")
flags.DEFINE_string("test_data", "", "Path to the test data.")

#Define columns
COLUMNS = ["encounter_id", "patient_nbr", "race", "gender", "age", "weight", "admission_type_id", "discharge_disposition_id", "admission_source_id", "time_in_hospital", "payer_code", "medical_specialty", "num_lab_procedures", "num_procedures", "num_medications", "number_outpatient", "number_emergency", "number_inpatient", "diag_1", "diag_2", "diag_3", "number_diagnoses", "max_glu_serum", "A1Cresult", "metformin", "repaglinide", "nateglinide", "chlorpropamide", "glimepiride", "acetohexamide", "glipizide", "glyburide", "tolbutamide", "pioglitazone", "rosiglitazone", "acarbose", "miglitol", "troglitazone", "tolazamide", "examide", "citoglipton", "insulin", "glyburidemetformin", "glipizidemetformin", "glimepiridepioglitazone", "metforminrosiglitazone", "metforminpioglitazone", "change", "diabetesMed", "readmitted"]

data = [[input_list[h] for h in range(0,50)]]

input_list = data
print(input_list)
df_test = pd.DataFrame(input_list, columns = COLUMNS)
print(df_test)
# df_test = df_test.append(input_list, ignore_index = True)

LABEL_COLUMN = "label"

CATEGORICAL_COLUMNS = ["race", "gender", "age", "weight", "admission_type_id", "discharge_disposition_id", "admission_source_id", "payer_code", "medical_specialty", "diag_1", "diag_2", "diag_3", "max_glu_serum", "A1Cresult", "metformin", "repaglinide", "nateglinide", "chlorpropamide", "glimepiride", "acetohexamide", "glipizide", "glyburide", "tolbutamide", "pioglitazone", "rosiglitazone", "acarbose", "miglitol", "troglitazone", "tolazamide", "examide", "citoglipton", "insulin", "glyburidemetformin", "glipizidemetformin", "glimepiridepioglitazone", "metforminrosiglitazone", "metforminpioglitazone", "change", "diabetesMed"]

CONTINUOUS_COLUMNS = ["time_in_hospital", "num_lab_procedures", "num_procedures", "num_medications", "number_outpatient", "number_emergency", "number_inpatient", "number_diagnoses"]

training_data_file = "Challenge_1_Training.csv"
test_data_file = "Challenge_1_Training.csv"


def build_estimator(model_dir): #Build an estimator

    #Define categorical base feature columns
    race = tf.contrib.layers.sparse_column_with_keys(column_name="race", keys=["Caucasian", "Asian", "AfricanAmerican", "Hispanic", "Other"])
    gender = tf.contrib.layers.sparse_column_with_keys(column_name="gender", keys=["Male", "Female"])
    age = tf.contrib.layers.sparse_column_with_keys(column_name="age", keys=["[0-10)", "[10-20)", "[20-30)", "[30-40)", "[40-50)", "[50-60)", "[60-70)", "[70-80)", "[80-90)", "[90-100)"])
    weight = tf.contrib.layers.sparse_column_with_keys(column_name="weight", keys=["[0-25)", "[25-50)", "[50-75)", "[75-100)", "[100-125)", "[125-150)", "[150-175)", "[175-200)", "?"])
    admission_type_id = tf.contrib.layers.sparse_column_with_keys(column_name="race", keys=["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    discharge_disposition_id = tf.contrib.layers.sparse_column_with_keys(column_name="race", keys=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"])
    admission_source_id = tf.contrib.layers.sparse_column_with_keys(column_name="race", keys=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"])
    payer_code = tf.contrib.layers.sparse_column_with_hash_bucket("payer_code", hash_bucket_size=1000)
    medical_specialty = tf.contrib.layers.sparse_column_with_hash_bucket("medical_specialty", hash_bucket_size=1000)
    diag_1 = tf.contrib.layers.sparse_column_with_hash_bucket("diag_1", hash_bucket_size=10000)
    diag_2 = tf.contrib.layers.sparse_column_with_hash_bucket("diag_2", hash_bucket_size=10000)
    diag_3 = tf.contrib.layers.sparse_column_with_hash_bucket("diag_3", hash_bucket_size=10000)
    max_glu_serum = tf.contrib.layers.sparse_column_with_keys(column_name="max_glu_serum", keys=[">200", ">300", "Normal", "None"])
    A1Cresult = tf.contrib.layers.sparse_column_with_keys(column_name="A1Cresult", keys=[">8", ">7", "Normal", "None"])
    metformin = tf.contrib.layers.sparse_column_with_keys(column_name="metformin", keys=["Up", "Down", "Steady", "No"])
    repaglinide = tf.contrib.layers.sparse_column_with_keys(column_name="repaglinide", keys=["Up", "Down", "Steady", "No"])
    nateglinide = tf.contrib.layers.sparse_column_with_keys(column_name="nateglinide", keys=["Up", "Down", "Steady", "No"])
    chlorpropamide = tf.contrib.layers.sparse_column_with_keys(column_name="chlorpropamide", keys=["Up", "Down", "Steady", "No"])
    glimepiride = tf.contrib.layers.sparse_column_with_keys(column_name="glimepiride", keys=["Up", "Down", "Steady", "No"])
    acetohexamide = tf.contrib.layers.sparse_column_with_keys(column_name="acetohexamide", keys=["Up", "Down", "Steady", "No"])
    glipizide = tf.contrib.layers.sparse_column_with_keys(column_name="glipizide", keys=["Up", "Down", "Steady", "No"])
    glyburide = tf.contrib.layers.sparse_column_with_keys(column_name="glyburide", keys=["Up", "Down", "Steady", "No"])
    tolbutamide = tf.contrib.layers.sparse_column_with_keys(column_name="tolbutamide", keys=["Up", "Down", "Steady", "No"])
    pioglitazone = tf.contrib.layers.sparse_column_with_keys(column_name="pioglitazone", keys=["Up", "Down", "Steady", "No"])
    rosiglitazone = tf.contrib.layers.sparse_column_with_keys(column_name="rosiglitazone", keys=["Up", "Down", "Steady", "No"])
    acarbose = tf.contrib.layers.sparse_column_with_keys(column_name="acarbose", keys=["Up", "Down", "Steady", "No"])
    miglitol = tf.contrib.layers.sparse_column_with_keys(column_name="miglitol", keys=["Up", "Down", "Steady", "No"])
    troglitazone = tf.contrib.layers.sparse_column_with_keys(column_name="troglitazone", keys=["Up", "Down", "Steady", "No"])
    tolazamide = tf.contrib.layers.sparse_column_with_keys(column_name="tolazamide", keys=["Up", "Down", "Steady", "No"])
    examide = tf.contrib.layers.sparse_column_with_keys(column_name="examide", keys=["Up", "Down", "Steady", "No"])
    citoglipton = tf.contrib.layers.sparse_column_with_keys(column_name="citoglipton", keys=["Up", "Down", "Steady", "No"])
    insulin = tf.contrib.layers.sparse_column_with_keys(column_name="insulin", keys=["Up", "Down", "Steady", "No"])
    glyburidemetformin = tf.contrib.layers.sparse_column_with_keys(column_name="glyburidemetformin", keys=["Up", "Down", "Steady", "No"])
    glipizidemetformin = tf.contrib.layers.sparse_column_with_keys(column_name="glipizidemetformin", keys=["Up", "Down", "Steady", "No"])
    glimepiridepioglitazone = tf.contrib.layers.sparse_column_with_keys(column_name="glimepiridepioglitazone", keys=["Up", "Down", "Steady", "No"])
    metforminrosiglitazone = tf.contrib.layers.sparse_column_with_keys(column_name="metforminrosiglitazone", keys=["Up", "Down", "Steady", "No"])
    metforminpioglitazone = tf.contrib.layers.sparse_column_with_keys(column_name="metforminpioglitazone", keys=["Up", "Down", "Steady", "No"])
    change = tf.contrib.layers.sparse_column_with_keys(column_name="change", keys=["Ch", "No"])
    diabetesMed = tf.contrib.layers.sparse_column_with_keys(column_name="diabetesMed", keys=["Yes", "No"])

    #Define continuous base feature columns
    time_in_hospital = tf.contrib.layers.real_valued_column("time_in_hospital")
    num_lab_procedures = tf.contrib.layers.real_valued_column("num_lab_procedures")
    num_procedures = tf.contrib.layers.real_valued_column("num_procedures")
    num_medications = tf.contrib.layers.real_valued_column("num_medications")
    number_outpatient = tf.contrib.layers.real_valued_column("number_outpatient")
    number_emergency = tf.contrib.layers.real_valued_column("number_emergency")
    number_inpatient = tf.contrib.layers.real_valued_column("number_inpatient")
    number_diagnoses = tf.contrib.layers.real_valued_column("number_diagnoses")

    #Define deep columns (categorical, then continuous)
    deep_columns = [
        tf.contrib.layers.embedding_column(race, dimension=10),
        tf.contrib.layers.embedding_column(gender, dimension=10),
        tf.contrib.layers.embedding_column(age, dimension=10),
        tf.contrib.layers.embedding_column(weight, dimension=10),
        tf.contrib.layers.embedding_column(admission_type_id, dimension=10),
        tf.contrib.layers.embedding_column(discharge_disposition_id, dimension=10),
        tf.contrib.layers.embedding_column(admission_source_id, dimension=10),
        tf.contrib.layers.embedding_column(payer_code, dimension=10),
        tf.contrib.layers.embedding_column(medical_specialty, dimension=10),
        tf.contrib.layers.embedding_column(diag_1, dimension=10),
        tf.contrib.layers.embedding_column(diag_2, dimension=10),
        tf.contrib.layers.embedding_column(diag_3, dimension=10),
        tf.contrib.layers.embedding_column(max_glu_serum, dimension=10),
        tf.contrib.layers.embedding_column(A1Cresult, dimension=10),
        tf.contrib.layers.embedding_column(metformin, dimension=10),
        tf.contrib.layers.embedding_column(repaglinide, dimension=10),
        tf.contrib.layers.embedding_column(nateglinide, dimension=10),
        tf.contrib.layers.embedding_column(chlorpropamide, dimension=10),
        tf.contrib.layers.embedding_column(glimepiride, dimension=10),
        tf.contrib.layers.embedding_column(acetohexamide, dimension=10),
        tf.contrib.layers.embedding_column(glipizide, dimension=10),
        tf.contrib.layers.embedding_column(glyburide, dimension=10),
        tf.contrib.layers.embedding_column(tolbutamide, dimension=10),
        tf.contrib.layers.embedding_column(pioglitazone, dimension=10),
        tf.contrib.layers.embedding_column(rosiglitazone, dimension=10),
        tf.contrib.layers.embedding_column(acarbose, dimension=10),
        tf.contrib.layers.embedding_column(miglitol, dimension=10),
        tf.contrib.layers.embedding_column(troglitazone, dimension=10),
        tf.contrib.layers.embedding_column(tolazamide, dimension=10),
        tf.contrib.layers.embedding_column(examide, dimension=10),
        tf.contrib.layers.embedding_column(citoglipton, dimension=10),
        tf.contrib.layers.embedding_column(insulin, dimension=10),
        tf.contrib.layers.embedding_column(glyburidemetformin, dimension=10),
        tf.contrib.layers.embedding_column(glipizidemetformin, dimension=10),
        tf.contrib.layers.embedding_column(glimepiridepioglitazone, dimension=10),
        tf.contrib.layers.embedding_column(metforminrosiglitazone, dimension=10),
        tf.contrib.layers.embedding_column(metforminpioglitazone, dimension=10),
        tf.contrib.layers.embedding_column(change, dimension=10),
        tf.contrib.layers.embedding_column(diabetesMed, dimension=10),
        time_in_hospital,
        num_lab_procedures,
        num_procedures,
        num_medications,
        number_outpatient,
        number_emergency,
        number_inpatient,
        number_diagnoses
    ]

    m = tf.contrib.learn.DNNClassifier(model_dir=model_dir, feature_columns=deep_columns, hidden_units=[200, 100, 50], n_classes=3)

    return m

def input_fn(df): #from tensorflow.org tutorial
    # Creates a dictionary mapping from each continuous feature column name (k) to
    # the values of that column stored in a constant Tensor.
    continuous_cols = {k: tf.constant(df[k].values) for k in CONTINUOUS_COLUMNS}
    # Creates a dictionary mapping from each categorical feature column name (k)
    # to the values of that column stored in a tf.SparseTensor.
    categorical_cols = {k: tf.SparseTensor(indices=[[i, 0] for i in range(df[k].size)], values=df[k].values, shape=[df[k].size, 1]) for k in CATEGORICAL_COLUMNS}
    # Merges the two dictionaries into one.
    feature_cols = {**continuous_cols, **categorical_cols}
    # Converts the label column into a constant Tensor.
    label = tf.constant(df[LABEL_COLUMN].values)
    # Returns the feature columns and the label.

    return feature_cols, label

def train_and_evaluate(): #Train model then evaluate model
    #df_test = pd.DataFrame([[22915332, 2345234, "Caucasian", "Female", "[80-90)", "?", 3, 1, 4, 5, "?", "?", 39, 3, 11, 0, 0, 0, "414", "289", "593", 7, "None", "None", "No", "No", "No", "No", "No", "No", "No", "Steady", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "Yes", ">30"]], columns = COLUMNS)
    #input_list = [[22915332, 2345234, "Caucasian", "Female", "[80-90)", "?", 3, 1, 4, 5, "?", "?", 39, 3, 11, 0, 0, 0, "414", "289", "593", 7, "None", "None", "No", "No", "No", "No", "No", "No", "No", "Steady", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "Yes", ">30"]]
    #df_test = pd.DataFrame(data=input_list, columns = COLUMNS)
    global df_test
    # remove NaN elements
    df_test = df_test.dropna(how='any', axis=0)

    df_test[LABEL_COLUMN] = (df_test["readmitted"].apply(lambda x: "<30" in x)).astype(int)

    model_dir = "/home/weston/Desktop/challenge_1/"
    print("model directory = %s" % model_dir)

    m = build_estimator(model_dir)

    prediction = m.predict(input_fn = lambda: input_fn(df_test))
    print("xxxxxxxxxx"+str(prediction)[1])

def main(_):
    train_and_evaluate()

sys.argv.clear()

if __name__ == "__main__":
    tf.app.run()