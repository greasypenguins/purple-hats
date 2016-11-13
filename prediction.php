<?php

$race = $_POST['race'];
$gender = $_POST['gender'];
$age = $_POST['age'];
$weight = $_POST['weight'];
$admission_type_id = $_POST['admission_type_id'];
$discharge_disposition_id = $_POST['discharge_disposition_id'];
$admission_source_id = $_POST['admission_source_id'];
$time_in_hospital = $_POST['time_in_hospital'];
$payer_code = $_POST['payer_code'];
$medical_specialty = $_POST['medical_specialty'];
$num_lab_procedures = $_POST['num_lab_procedures'];
$num_procedures = $_POST['num_procedures'];
$num_medications = $_POST['num_medications'];
$number_outpatient = $_POST['number_outpatient'];
$number_emergency = $_POST['number_emergency'];
$number_inpatient = $_POST['number_inpatient'];
$diag_1 = $_POST['diag_1'];
$diag_2 = $_POST['diag_2'];
$diag_3 = $_POST['diag_3'];
$number_diagnoses = $_POST['number_diagnoses'];
$max_glu_serum = $_POST['max_glu_serum'];
$A1Cresult = $_POST['A1Cresult'];
$metformin = $_POST['metformin'];
$repaglinide = $_POST['repaglinide'];
$nateglinide = $_POST['nateglinide'];
$chlorpropamide = $_POST['chlorpropamide'];
$glimepiride = $_POST['glimepiride'];
$acetohexamide = $_POST['acetohexamide'];
$glipizide = $_POST['glipizide'];
$glyburide = $_POST['glyburide'];
$tolbutamide = $_POST['tolbutamide'];
$pioglitazone = $_POST['pioglitazone'];
$rosiglitazone = $_POST['rosiglitazone'];
$acarbose = $_POST['acarbose'];
$miglitol = $_POST['miglitol'];
$troglitazone = $_POST['troglitazone'];
$tolazamide = $_POST['tolazamide'];
$examide = $_POST['examide'];
$citoglipton = $_POST['citoglipton'];
$insulin = $_POST['insulin'];
$glyburidemetformin = $_POST['glyburidemetformin'];
$glipizidemetformin = $_POST['glipizidemetformin'];
$glimepiridepioglitazone = $_POST['glimepiridepioglitazone'];
$metforminrosiglitazone = $_POST['metforminrosiglitazone'];
$metforminpioglitazone = $_POST['metforminpioglitazone'];
$change = $_POST['change'];
$diabetesMed = $_POST['diabetesMed'];


echo ('<br />');

#$python = escapeshellcmd("python3 /var/www/tensorflow/tf_dnn_eval.py $race $gender $age $weight $admission_type_id $discharge_disposition_id $admission_source_id $time_in_hospital $payer_code $medical_specialty $num_lab_procedures $num_procedures $num_medications $number_outpatient $number_emergency $number_inpatient $diag_1 $diag_2 $diag_3 $number_diagnoses $max_glu_serum $A1Cresult $metformin $repaglinide $nateglinide $chlorpropamide $glimepiride $acetohexamide $glipizide $glyburide $tolazamide $pioglitazone $rosiglitazone $acarbose $miglitol $troglitazone $examide $citoglipton $insulin $glyburidemetformin $glipizidemetformin $glimepiridepioglitazone $metforminpioglitazone $metforminrosiglitazone $change $diabetesMed");

#$python = "python3 /var/www/tensorflow/tf_dnn_eval.py 22915332 1475073 $race $gender $age $weight $admission_type_id $discharge_disposition_id $admission_source_id $time_in_hospital $payer_code $medical_specialty $num_lab_procedures $num_procedures $num_medications $number_outpatient $number_emergency $number_inpatient $diag_1 $diag_2 $diag_3 $number_diagnoses $max_glu_serum $A1Cresult $metformin $repaglinide $nateglinide $chlorpropamide $glimepiride $acetohexamide $glipizide $glyburide $tolazamide $pioglitazone $rosiglitazone $acarbose $miglitol $troglitazone $examide $citoglipton $insulin $glyburidemetformin $glipizidemetformin $glimepiridepioglitazone $metforminpioglitazone $metforminrosiglitazone $change $diabetesMed";

$python = "python3 /var/www/tensorflow/tf_dnn_eval.py $race $gender $age $weight $admission_type_id $discharge_disposition_id $admission_source_id $time_in_hospital $payer_code $medical_specialty $num_lab_procedures $num_procedures $num_medications $number_outpatient $number_emergency $number_inpatient $diag_1 $diag_2 $diag_3 $number_diagnoses $max_glu_serum $A1Cresult $metformin $repaglinide $nateglinide $chlorpropamide $glimepiride $acetohexamide $glipizide $glyburide $tolbutamide $pioglitazone $rosiglitazone $acarbose $miglitol $troglitazone $tolazamide $examide $citoglipton $insulin $glyburidemetformin $glipizidemetformin $glimepiridepioglitazone $metforminrosiglitazone $metforminpioglitazone $change $diabetesMed";

#python3 /var/www/tensorflow/tf_dnn_eval.py Caucasian Male [0-10 ? 1 1 1 546 MC 456 465 654 456 64 65 654 654 654 654 64 >300 >7 Up No No No No No No No No No No Down No No No No No No No No No No Up No Yes


#$python = "date";

#47 + file name

echo $python;
echo ('<br />');
echo ('<br />');
echo ('<br />');

$output = shell_exec($python);
echo $output;


$shell = "$output | cut -d'xxxxxxxxxx' -f2";
$final = shell_exec($shell);

echo ('<br />');
echo $final;
echo ('Prediction Completed');
echo ('<br />');
echo ('<br />');

if($final=='1')
{
	echo ('<h2>Patient is likely to return within 30 days</h2>');
}
else if($final=='0')
{
	echo ('<h2>Patient is not likely to return within 30 days</h2>');	
}
else
{
	echo ('<h2>There was an error with the program, ensure all fields are filled out</h2>');	
}


?>
