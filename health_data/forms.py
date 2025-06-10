from django import forms
from .models import HealthRecord

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        exclude = ['user', 'date_recorded']
        #fields = ['date_measured', 'height', 'weight', 'waist_line', 'systolic_bp']
        widgets = {
            'date_measured': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'date_measured': '검사일',
            'height': '키 (cm)',
            'weight': '몸무게 (kg)',
            'waist_line': '허리둘레 (cm)',
            'systolic_bp': '수축기 혈압 (Systolic BP: mmHg)',
            'diastolic_bp': '이완기 혈압 (Diastolic BP: mmHg)',

            # Eye
            'ocular_tension_left': '안압 (좌, mmHg)',
            'ocular_tension_right': '안압 (우, mmHg)',
            'fundus': '안저 소견 (Fundus)',

            # Hearing
            'hearing': '청력 소견 (Hearing)',

            # EKG
            'ekg': '심전도 (EKG)',

            # Imaging
            'gastroscopy': '위내시경 소견',
            'abdominal_sono': '상복부 초음파 소견',
            'thyroid_sono': '갑상선 초음파 소견',
            'male_pelvis_sono': '남성하복부 초음파 소견',
            'chest_xray_ct': '흉부 촬영',

            # Diabetes Test
            'glucose': '혈당 (Glucose)',

            # Liver Panel
            'total_protein': '총 단백질 (g/dL)',
            'albumin': '알부민 (Albumin: g/dL)',
            'globulin': '글로불린 (Globulin: g/dL)',
            't_bilirubin': '총 빌리루빈 (T.Bilirubin: mg/dL)',
            'd_bilirubin': '직접 빌리루빈 (D.Bilirubin: mg/dL)',
            'sgot_ast': '혈청GOT (SGOT(AST): U/L)',
            'sgpt_alt': '혈청GPT (SGPT(ALT): U/L)',
            'alk_phosphatase': '알칼리포스파타제 (Alk.phosphatase: U/L)',
            'ggtp': '감마GTP: U/L',
            'ag_ratio': 'A/G 비율 (A/G Ratio)',
            'bilirubin_indirect': '간접 빌리루빈 (mg/dL)',
            'hbsag': 'B형 간염 항원 (HBsAg(ECLIA): COI)',
            'hbsab': 'B형 간염 항체 (HBsAb(ECLIA): IU/L)',

            # Kidney and metabolic
            'ldh': '젖산탈수소효소 (LDH: U/L)',
            'bun': '요소질소 (BUN: mg/dL)',
            'creatinine': '크레아티닌 (Creatinine: mg/dL)',
            'egfr': '신사구체여과율 (e-GFR: mL/min/1.73㎡)',
            'bc_ratio': 'BUN/Cr 비율 (B/C ratio)',

            # Lipids and diabetes
            'cholesterol_total': '총 콜레스테롤 (mg/dL)',
            'cholesterol_ldl': 'LDL 콜레스테롤 (mg/dL)',
            'cholesterol_hdl': 'HDL 콜레스테롤 (mg/dL)',
            'triglyceride': '중성지방 (mg/dL)',

            # Other Infectious Diseases
            'rpr': '매독검사 (RPR)',

            # Hematology
            'wbc': '백혈구수 (WBC: ×10³/μL)',
            'segment': '중성구백분율 (Segment: %)',
            'band': '간상구백분율 (Band: %)',
            'lymphocyte': '임파구백분율 (Lymphocyte: %)',
            'monocyte': '단구백분율 (Monocyte: %)',
            'eosinophil': '호산구백분율 (Eosinophil: %)',
            'basophil': '염기구백분율 (Basophil: %)',
            'nucleated_rbc': '유핵적혈구수 (Nucleated RBC: /100WBCs)',
            'blast': '골수아구 (Blast: %)',
            'promyelocyte': '전골수구수 (Promyelocyte: %)',
            'myelocyte': '골수구수 (Myelocyte: %)',
            'metamyelocyte': '후골수구수 (Metamyelocyte: %)',
            'rbc': '적혈구수 (RBC: ×10⁶/μL)',
            'hemoglobin': '혈색소 (Hemoglobin: g/dL)',
            'hct': '혈구용적치 (HCT: %)',
            'mcv': '평균적혈구용적 (MCV: fL)',
            'mch': '적혈구혈색소 (MCH: pg)',
            'mchc': '적혈구혈색농도 (MCHC: %)',
            'rdw': '적혈구분포폭 (RDW: %)',
            'platelet': '혈소판수 (Platelet: ×10³/μL)',
            'pct': '혈소판크리트 (PCT: %)',
            'mpv': '평균혈소판용적 (MPV: fL)',
            'pdw': '혈소판분포폭 (PDW :%)',

            # Gout & Rheumatoid Arthritis
            'uric_acid': '요산 (Uric acid: mg/dL)',
            'ra_factor': '류마티스 인자 (RA factor: IU/mL)',


            # Cancer Markers
            'afp': '알파태아단백 (AFP(ECLIA): ng/mL)',
            'cea': '태아성암항원 (CEA: ng/mL)',
            'psa': '전립선특이항원 (PSA: ng/mL)',
            'ca199': '암항원 (CA 19-9: U/mL)',

            # Thyroid
            'tsh': '갑상선자극호르몬: (TSH: µIU/mL)',
            'free_t4': '갑상선 Free T4 (ng/dL)',

            # Stool test
            'stool_occult_blood': '분변 잠혈 반응',

            # Urinalysis
            'urine_color': '소변 색',
            'urine_sg': '소변 비중',
            'urine_ph': '소변 산도 (pH)',
            'urine_protein': '소변 단백',
            'urine_glucose': '소변 포도당',
            'urine_ketone': '소변 케톤체 (Ketone Bodies)',
            'urine_bilirubin': '소변 빌리루빈 (Bilirubin)',
            'urine_nitrite': '소변 아질산염 (Nitrite)',
            'urine_blood': '요잠혈 (Blood)',
            'urine_urobilinogen': '소변 우로빌리노겐 (Urobilinogen)',
            'urine_rbc': '소변 적혈구 (개/HPF)',
            'urine_wbc': '소변 백혈구 (개/HPF)',
            'urine_epithelial_cell': '소변 상피세포 (개/HPF)',
            'urine_casts': '소변 원주',
            'urine_bacteria': '소변 세균',
            'urine_crystals': '소변 결정체',
            'urine_other': '소변 기타',

            # InBody composition
            'body_water': '체수분 (L)',
            'body_protein': '단백질량 (kg)',
            'body_minerals': '무기질량 (kg)',
            'body_fat_mass': '체지방량 (kg)',
            'skeletal_muscle_mass': '골격근량 (kg)',
            'percent_body_fat': '체지방률 (%)',
            'ecw_ratio': '세포외수분비율 (ECW/TBW)',

            # Segmental lean analysis
            'right_arm': '오른팔 근육량 (kg)',
            'left_arm': '왼팔 근육량 (kg)',
            'trunk': '몸통 근육량 (kg)',
            'right_leg': '오른다리 근육량 (kg)',
            'left_leg': '왼다리 근육량 (kg)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

