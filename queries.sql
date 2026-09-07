select * from diagnoses;
select * from labs;
select * from outcomes;
select * from patients;

-- Retrieve detailed patient lab history
-- Retrieve Detailed Patient Lab History
SELECT 
    p.patient_id,
    p.name,
    d.diagnosis_name,
    o.outcome_name,
    l.test_name,
    l.result,
    l.normal_range
FROM patients p
JOIN diagnoses d 
    ON p.diagnosis_id = d.diagnosis_id
JOIN outcomes o 
    ON p.outcome_id = o.outcome_id
JOIN labs l 
    ON p.patient_id = l.patient_id
ORDER BY p.patient_id, l.test_name;


-- Average lab results by diagnosis
SELECT 
    d.diagnosis_name,
    l.test_name,
    ROUND(AVG(l.result), 2) AS avg_result
FROM patients p
JOIN diagnoses d 
    ON p.diagnosis_id = d.diagnosis_id
JOIN labs l 
    ON p.patient_id = l.patient_id
GROUP BY 
    d.diagnosis_name,
    l.test_name
ORDER BY 
    d.diagnosis_name,
    l.test_name;

-- Count of abnormal lab results 
SELECT 
    p.patient_id,
    p.name,
    COUNT(*) AS abnormal_count
FROM patients p
JOIN labs l 
    ON p.patient_id = l.patient_id
WHERE 
    (l.test_name = 'Blood Sugar' AND l.result > 120)
    OR
    (l.test_name = 'Cholesterol' AND l.result > 200)
    OR
    (l.test_name = 'Hemoglobin' AND l.result < 13)
GROUP BY 
    p.patient_id,
    p.name
ORDER BY 
    abnormal_count DESC;

-- Diagnoses with highest treatment costs
SELECT 
    d.diagnosis_name,
    SUM(p.treatment_cost) AS total_cost
FROM patients p
JOIN diagnoses d
    ON p.diagnosis_id = d.diagnosis_id
GROUP BY d.diagnosis_name
ORDER BY total_cost DESC;

-- Patients at risk by age and gender
SELECT 
    p.patient_id,
    p.name,
    p.age,
    d.diagnosis_name,
    o.outcome_name
FROM patients p
JOIN diagnoses d 
    ON p.diagnosis_id = d.diagnosis_id
JOIN outcomes o 
    ON p.outcome_id = o.outcome_id
WHERE p.age > 65
  AND p.gender = 'M'
  AND o.outcome_name != 'Recovered';

-- Lab trends over time for a specific patient
SELECT 
    l.test_name,
    l.result,
    p.admission_date
FROM labs l
JOIN patients p 
    ON l.patient_id = p.patient_id
WHERE p.patient_id IN (2, 4, 6, 8, 10, 12)
ORDER BY p.admission_date;

-- Distribution of Outcomes by Diagnosis
SELECT 
    d.diagnosis_name,
    o.outcome_name,
    COUNT(*) AS outcome_count
FROM patients p
JOIN diagnoses d 
    ON p.diagnosis_id = d.diagnosis_id
JOIN outcomes o 
    ON p.outcome_id = o.outcome_id
GROUP BY 
    d.diagnosis_name,
    o.outcome_name
ORDER BY 
    d.diagnosis_name,
    o.outcome_name DESC;
