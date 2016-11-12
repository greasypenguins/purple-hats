from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np

training_data_csv = "Challenge_1_Training.csv"
test_data_csv = "Challenge_1_Training.csv"

#training_set = tf.contrib.learn.datasets.base.load_csv(filename=training_data_csv, target_dtype=np.int)

# Categorical base columns.
race = tf.contrib.layers.sparse_column_with_keys(column_name="race", keys=["Caucasian", "Asian", "AfricanAmerican", "Hispanic", "Other"])
gender = tf.contrib.layers.sparse_column_with_keys(column_name="gender", keys=["Male", "Female"])
age = tf.contrib.layers.sparse_column_with_keys(column_name="age", keys=["[0-10)", "[10-20)", "[20-30)", "[30-40)", "[40-50)", "[50-60)", "[60-70)", "[70-80)", "[80-90)", "[90-100)"])
weight = tf.contrib.layers.sparse_column_with_keys(column_name="weight", keys=["[0-25)", "[25-50)", "[50-75)", "[75-100)", "[100-125)", "[125-150)", "[150-175)", "[175-200)", "?"])
admission_type_id = tf.contrib.layers.sparse_column_with_hash_bucket("admission_type_id", hash_bucket_size=1000)
discharge_disposition_id = tf.contrib.layers.sparse_column_with_hash_bucket("discharge_disposition_id", hash_bucket_size=1000)
admission_source_id = tf.contrib.layers.sparse_column_with_hash_bucket("admission_type_id", hash_bucket_size=1000)
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
glyburide.metformin = tf.contrib.layers.sparse_column_with_keys(column_name="glyburide.metformin", keys=["Up", "Down", "Steady", "No"])
glipizide.metformin = tf.contrib.layers.sparse_column_with_keys(column_name="glipizide.metformin", keys=["Up", "Down", "Steady", "No"])
glimepiride.pioglitazone = tf.contrib.layers.sparse_column_with_keys(column_name="glimepiride.pioglitazone", keys=["Up", "Down", "Steady", "No"])
metformin.rosiglitazone = tf.contrib.layers.sparse_column_with_keys(column_name="metformin.rosiglitazone", keys=["Up", "Down", "Steady", "No"])
metformin.pioglitazone = tf.contrib.layers.sparse_column_with_keys(column_name="metformin.pioglitazone", keys=["Up", "Down", "Steady", "No"])
change = tf.contrib.layers.sparse_column_with_keys(column_name="change", keys=["Ch", "No"])
diabetesMed = tf.contrib.layers.sparse_column_with_keys(column_name="diabetesMed", keys=["Yes", "No"])

# Continuous base columns.
time_in_hospital = tf.contrib.layers.real_valued_column("time_in_hospital")
num_lab_procedures = tf.contrib.layers.real_valued_column("num_lab_procedures")
num_procedures = tf.contrib.layers.real_valued_column("num_procedures")
num_medications = tf.contrib.layers.real_valued_column("num_medications")
number_outpatient = tf.contrib.layers.real_valued_column("number_outpatient")
number_emergency = tf.contrib.layers.real_valued_column("number_emergency")
number_inpatient = tf.contrib.layers.real_valued_column("number_inpatient")
number_diagnoses = tf.contrib.layers.real_valued_column("number_diagnoses")






