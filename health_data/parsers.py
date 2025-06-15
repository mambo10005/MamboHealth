from PyPDF2 import PdfReader

def parse_hospital_a(text):
    FIELD_MAP = {
        "혈당": "glucose",
        "총콜레스테롤": "cholesterol_total",
        "HDL": "cholesterol_hdl",
        "LDL": "cholesterol_ldl",
        "중성지방": "triglyceride",
        "신장": "height",
        "체중": "weight",
        "수축기혈압": "systolic_bp",
        "이완기혈압": "diastolic_bp",
        "측정일": "date_measured",
    }
    result = {}
    for line in text.splitlines():
        for label, field in FIELD_MAP.items():
            if label in line:
                value = ''.join(filter(lambda x: x.isdigit() or x == '.' or x == '-', line.split()[-1]))
                result[field] = value
    return result


def parse_hospital_b(text):
    FIELD_MAP = {
        "Glucose": "glucose",
        "Total Cholesterol": "cholesterol_total",
        "HDL": "cholesterol_hdl",
        "LDL": "cholesterol_ldl",
        "Triglyceride": "triglyceride",
        "Height": "height",
        "Weight": "weight",
        "Systolic BP": "systolic_bp",
        "Diastolic BP": "diastolic_bp",
        "Date": "date_measured",
    }
    result = {}
    for line in text.splitlines():
        for label, field in FIELD_MAP.items():
            if label in line:
                value = ''.join(filter(lambda x: x.isdigit() or x == '.' or x == '-', line.split()[-1]))
                result[field] = value
    return result

def parse_pdf_to_health_data(file):
    reader = PdfReader(file)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)

    data = parse_hospital_a(text)
    if not data or len(data) < 3:
        data = parse_hospital_b(text)
    return data or {}

