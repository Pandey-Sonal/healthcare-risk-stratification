CREATE TABLE diagnoses (
    diagnosis_id INT PRIMARY KEY,
    diagnosis_name VARCHAR(55)
);

CREATE TABLE outcomes (
    outcome_id INT PRIMARY KEY,
    outcome_name VARCHAR(255)
);

CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR(1),
    diagnosis_id INT,
    admission_date DATE,
    discharge_date DATE,
    outcome_id INT,
    treatment_cost DECIMAL(18,2),

    FOREIGN KEY (diagnosis_id)
        REFERENCES diagnoses(diagnosis_id),

    FOREIGN KEY (outcome_id)
        REFERENCES outcomes(outcome_id)
);

CREATE TABLE labs (
    lab_id INT PRIMARY KEY,
    patient_id INT,
    test_name VARCHAR(255),
    result DECIMAL(10,2),
    normal_range VARCHAR(255),

    FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id)
);