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


$python = escapeshellcmd('python3 script.py $race $gender $age $weight $admission_type_id $discharge_disposition_id $admission_source_id $time_in_hospital $payer_code $medical_specialty $num_lab_procedures $num_procedures $num_medications $number_outpatient $number_emergency $number_inpatient $diag_1 $diag_2 $diag_3 $number_diagnoses $max_glu_serum $A1Cresult $metformin $repaglinide $nateglinide $chlorpropamide $glimepiride $acetohexamide $glipizide $glyburide $tolazamide $pioglitazone $rosiglitazone $acarbose $miglitol $troglitazone $examide $citoglipton $insulin $glyburidemetformin $glipizidemetformin $glimepiridepioglitazone $metforminpioglitazone $metforminrosiglitazone');

$output = shell_exec($python);
echo $output;



?>
