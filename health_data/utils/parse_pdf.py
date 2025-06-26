# health_data/utils/parse_pdf.py
import pdfplumber
import re
from datetime import datetime

def parse_labcorp_pdf(file_path):
    data = {}
    with pdfplumber.open(file_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

    # Extract date_measured
    date_match = re.search(r"Date Collected:\s*(\d{2}/\d{2}/\d{4})", text)
    if date_match:
        data['date_measured'] = datetime.strptime(date_match.group(1), '%m/%d/%Y').date()

    def extract_value(pattern, unit=None, cast=float):
        match = re.search(pattern, text)
        if match:
            try:
                return cast(match.group(1).replace(',', '').strip())
            except ValueError:
                return None
        return None

    # Basic Panel
    data['tsh'] = extract_value(r'TSH.*?([\d.]+)\s+uIU/mL')
    data['free_t4'] = extract_value(r'T4,Free\(Direct\).*?([\d.]+)\s+ng/dL')
    data['vitamin_d'] = extract_value(r'Vitamin D, 25-Hydroxy.*?([\d.]+)\s+ng/mL')
    data['glucose'] = extract_value(r'Glucose\s+01\s+([\d.]+)\s+mg/dL')
    data['bun'] = extract_value(r'BUN\s+01\s+([\d.]+)\s+mg/dL')
    data['creatinine'] = extract_value(r'Creatinine\s+01\s+([\d.]+)\s+mg/dL')
    data['egfr'] = extract_value(r'eGFR\s+([\d.]+)')
    data['cholesterol_total'] = extract_value(r'Cholesterol, Total\s+01\s+([\d.]+)')
    data['cholesterol_hdl'] = extract_value(r'HDL Cholesterol\s+01\s+([\d.]+)')
    data['cholesterol_ldl'] = extract_value(r'LDL Chol Calc \(NIH\)\s+([\d.]+)')
    data['triglyceride'] = extract_value(r'Triglycerides\s+01\s+([\d.]+)')
    data['hba1c'] = extract_value(r'Hemoglobin A1c\s+01\s+([\d.]+)\s+%')
    data['psa'] = extract_value(r'Prostate Specific Ag\s+01\s+([\d.]+)\s+ng/mL')
    data['albumin'] = extract_value(r'Albumin\s+01\s+([\d.]+)\s+g/dL')
    data['wbc'] = extract_value(r'WBC\s+01\s+([\d.]+)')
    data['rbc'] = extract_value(r'RBC\s+01\s+([\d.]+)')
    data['hemoglobin'] = extract_value(r'Hemoglobin\s+01\s+([\d.]+)')
    data['hct'] = extract_value(r'Hematocrit\s+01\s+([\d.]+)')
    data['mcv'] = extract_value(r'MCV\s+01\s+([\d.]+)')
    data['mch'] = extract_value(r'MCH\s+01\s+([\d.]+)')
    data['mchc'] = extract_value(r'MCHC\s+01\s+([\d.]+)')
    data['rdw'] = extract_value(r'RDW\s+01\s+([\d.]+)')
    data['platelet'] = extract_value(r'Platelets\s+01\s+([\d.]+)')

    # Urinalysis
    data['urine_color'] = extract_value(r'Urine-Color\s+01\s+(\w+)', cast=str)
    data['urine_ph'] = extract_value(r'pH\s+01\s+([\d.]+)')
    data['urine_protein'] = extract_value(r'Protein\s+01\s+(\w+)', cast=str)
    data['urine_glucose'] = extract_value(r'Glucose\s+01\s+(\w+)', cast=str)
    data['urine_wbc'] = extract_value(r'WBC\s+01\s+(None seen|\d+)', cast=str)
    data['urine_rbc'] = extract_value(r'RBC\s+01\s+(None seen|\d+)', cast=str)
    data['urine_epithelial_cell'] = extract_value(r'Epithelial Cells.*?01\s+(None seen|\d+)', cast=str)
    data['urine_bacteria'] = extract_value(r'Bacteria\s+01\s+(None seen|Few)', cast=str)

    return data
