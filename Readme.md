

## 🏦 Bank Account & IFSC Code Validation

### 📘 Overview

This project validates **bank account numbers** and **IFSC codes** from a dataset to ensure data accuracy and consistency.
It performs **data cleaning**, **validation**, **summary generation**, and **visualization (pie chart)** to analyze the results.

---

### 🚀 Features

✅ Cleans and standardizes raw data (removes spaces, duplicates, and missing values)
✅ Validates **Account Numbers** (length, digits, repetition, sequence)
✅ Validates **IFSC Codes** (format, structure, known bank prefixes)
✅ Generates **summary report** of valid/invalid/missing records
✅ Visualizes the results using a **pie chart**

---

### 🧰 Technologies Used

* **Python 3**
* **Pandas** – for data processing
* **Regex (re)** – for pattern matching
* **Matplotlib** – for visualization

---

### 📂 Project Structure

```
📦 Bank_Account_IFSC_Code_Validation/
│
├── Bank_Acc_IFSC_Code_Validation.py       # Main script file
├── IFSC_Account_Validation_Dataset.csv    # Input dataset
├── Bank_Acc_Ifsc_Valid_Result.csv         # Output with validation results
├── Bank_Acc_Ifsc_Valid_Summary.csv        # Summary statistics
└── Validation_Summary_Pie_Chart.png       # Pie chart visualization
```

---

### 🧹 Data Cleaning Steps

1. Converted columns (`Account_Number`, `IFSC_Code`, `Customer_Name`, `Branch`) to **string** type.
2. Removed **extra spaces**, standardized to **uppercase/title case**.
3. Dropped **missing (`NaN`)** and **empty** values.
4. Removed **duplicates** based on `Account_Number`.

---

### 🧮 Validation Logic

#### 🏦 **Bank Account Number Validation**

A record is considered **Valid** if:

1. Length is between **9 and 18 digits**.
2. Contains only **digits (0–9)**.
3. Does **not** contain continuous numeric sequences (e.g., `123456`).
4. Does **not** contain adjacent repeated digits (e.g., `111111`).

#### 💳 **IFSC Code Validation**

A record is considered **Correct** if:

1. Length = **11 characters**.
2. All uppercase.
3. Matches the pattern `^[A-Z]{4}0[A-Z0-9]{6}$`.
4. First 4 letters (bank code) exist in known list:
   `['SBIN', 'HDFC', 'ICIC', 'AXIS', 'PNB', 'YESB', 'KARB']`

---

### 📊 Summary Output

The script generates a summary showing:

| Metric                      | Description                      |
| --------------------------- | -------------------------------- |
| **Total Processed Records** | Number of records in dataset     |
| **Valid Records**           | Account + IFSC both valid        |
| **Invalid Records**         | Records failing validation rules |
| **Missing Records**         | Empty or dropped entries         |




### 📤 Output Files

* `Bank_Acc_Ifsc_Valid_Result.csv` → Contains each record with its **ACC_No_Check** and **IFSc_Check**
* `Bank_Acc_Ifsc_Valid_Summary.csv` → Summary statistics
* `Validation_Summary_Pie_Chart.png` → Visualization image

---

### 🧩 Example Output

| Customer_Name | Account_Number | IFSC_Code   | Status   | Message |
| ------------- | -------------- | ----------- | -------- | ------- |
| Sita Sharma   | 105736437      | ICIC00LB3R9 | In Valid | Correct |
| Raj Kumar     | 9876543210     | SBIN0001234 | Valid    | Correct |


