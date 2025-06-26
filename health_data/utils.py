from django.forms.models import model_to_dict

def get_field_groups():
    return {
        "신체 측정": [
            "date_measured", "height", "weight", "waist_line", "systolic_bp", "diastolic_bp", "bmi"
        ],
        "안과": ["ocular_tension_left", "ocular_tension_right", "fundus"],
        "청력": ["hearing"],
        "심전도": ["ekg"],
        "내시경": ["gastroscopy"],
        "영상 검사": [
            "abdominal_sono", "thyroid_sono", "male_pelvis_sono", "chest_xray_ct",
            "carotid_artery_sono", "l_spine_ct", "c_spine_ct"
        ],
        "당뇨 검사": ["glucose", "hb_a1c"],
        "간 기능": [
            "total_protein", "albumin", "globulin", "t_bilirubin", "d_bilirubin", "sgpt_alt", "sgot_ast",
            "alk_phosphatase", "ggtp", "ag_ratio", "bilirubin_indirect", "hbsag", "hbsab", "anti_hcv", "hav_lgm"
        ],
        "신장 및 대사": ["bun", "creatinine", "egfr", "bc_ratio"],
        "전해질 및 비타민": ["sodium", "potassium", "chloride", "calcium", "phosphorus", "carbon_dioxide", "vitamin_d", "vitamin_b12", "serum_folate"],
        "근육 효소": ["ck_mb", "ldh"],
        "자율신경 및 스트레스": ["autonomic_nervous_balance", "autonomic_nervous_activity", "stress_index"],
        "골다공증": ["bone_density"],
        "지질": ["cholesterol_total", "cholesterol_ldl", "cholesterol_vldl", "cholesterol_hdl", "triglyceride"],
        "감염 질환": ["rpr"],
        "혈액 검사": [
            "wbc", "segment", "band", "lymphocyte", "monocyte", "eosinophil", "basophil",
            "nucleated_rbc", "blast", "promyelocyte", "myelocyte", "metamyelocyte",
            "rbc", "hemoglobin", "hct", "mcv", "mch", "mchc", "rdw",
            "platelet", "pct", "mpv", "pdw",
            "absolute_neutrophil_count", "absolute_lymphocyte_count", "absolute_monocyte_count",
            "absolute_eosinophil_count", "absolute_basophil_count", "immature_granulocyte", "absolute_immature_granulocyte_count"
        ],
        "통풍 및 류마티스": ["uric_acid", "ra_factor", "c_reactive_protein"],
        "암 표지자": ["afp", "cea", "psa", "ca199"],
        "갑상선": ["tsh", "free_t4"],
        "대변 검사": ["stool_occult_blood"],
        "소변 검사": [
            "urine_color", "urine_sg", "urine_ph", "urine_protein", "urine_glucose", "urine_ketone",
            "urine_bilirubin", "urine_nitrite", "urine_blood", "urine_urobilinogen", "urine_rbc", "urine_wbc_esterase",
            "urine_wbc", "urine_epithelial_cell", "urine_casts", "urine_bacteria", "urine_crystals", "urine_other"
        ],
        "체성분": [
            "body_water", "body_protein", "body_minerals", "body_fat_mass", "skeletal_muscle_mass",
            "percent_body_fat", "ecw_ratio"
        ],
        "부위별 근육량": ["right_arm", "left_arm", "trunk", "right_leg", "left_leg"],
    }

def get_disease_related_field_groups():
    return {
        "측정일": [  # General or Miscellaneous
            "date_measured"
        ],
        "심혈관질환": [  # Cardiovascular Disease
            "cholesterol_total", "cholesterol_ldl", "cholesterol_vldl", "cholesterol_hdl", "triglyceride",
            "systolic_bp", "diastolic_bp", "ekg", "ldh", "ck_mb"
        ],
        "당뇨": [  # Diabetes
            "glucose", "hb_a1c"
        ],
        "간질환": [  # Liver Disease
            "total_protein", "albumin", "globulin", "t_bilirubin", "d_bilirubin", "bilirubin_indirect",
            "sgpt_alt", "sgot_ast", "alk_phosphatase", "ggtp", "ag_ratio", "hbsag", "hbsab", "anti_hcv", "hav_lgm"
        ],
        "신장질환 및 대사": [  # Kidney Disease & Metabolism
            "bun", "creatinine", "egfr", "bc_ratio"
        ],
        "전해질 및 비타민 결핍": [  # Electrolyte/Vitamin Imbalance
            "sodium", "potassium", "chloride", "calcium", "phosphorus", "carbon_dioxide",
            "vitamin_d", "vitamin_b12", "serum_folate"
        ],
        "골격근질환": [  # Muscle Disorders
            "ck_mb", "ldh",  # Also under 심혈관질환, but relevant here too
            "skeletal_muscle_mass", "right_arm", "left_arm", "trunk", "right_leg", "left_leg"
        ],
        "스트레스 및 자율신경": [  # Stress & Autonomic Nervous System
            "autonomic_nervous_balance", "autonomic_nervous_activity", "stress_index"
        ],
        "골다공증": [  # Osteoporosis
            "bone_density"
        ],
        "비만 및 체성분": [  # Obesity & Body Composition
            "height", "weight", "waist_line", "bmi",
            "body_water", "body_protein", "body_minerals", "body_fat_mass",
            "percent_body_fat", "ecw_ratio"
        ],
        "감염 및 면역질환": [  # Infectious and Immune Diseases
            "rpr", "ra_factor", "c_reactive_protein", "anti_hcv", "hav_lgm", "hbsag", "hbsab"
        ],
        "혈액질환": [  # Hematologic Conditions
            "wbc", "segment", "band", "lymphocyte", "monocyte", "eosinophil", "basophil",
            "nucleated_rbc", "blast", "promyelocyte", "myelocyte", "metamyelocyte",
            "rbc", "hemoglobin", "hct", "mcv", "mch", "mchc", "rdw",
            "platelet", "pct", "mpv", "pdw",
            "absolute_neutrophil_count", "absolute_lymphocyte_count", "absolute_monocyte_count",
            "absolute_eosinophil_count", "absolute_basophil_count", "immature_granulocyte",
            "absolute_immature_granulocyte_count"
        ],
        "암 표지자": [  # Cancer Markers
            "afp", "cea", "psa", "ca199"
        ],
        "갑상선질환": [  # Thyroid Disease
            "tsh", "free_t4"
        ],
        "안과질환": [  # Ophthalmology
            "ocular_tension_left", "ocular_tension_right", "fundus"
        ],
        "청력장애": [  # Hearing Disorders
            "hearing"
        ],
        "위장관질환": [  # Gastrointestinal
            "gastroscopy", "stool_occult_blood"
        ],
        "비뇨기계질환": [  # Urinary System
            "urine_color", "urine_sg", "urine_ph", "urine_protein", "urine_glucose", "urine_ketone",
            "urine_bilirubin", "urine_nitrite", "urine_blood", "urine_urobilinogen", "urine_rbc",
            "urine_wbc_esterase", "urine_wbc", "urine_epithelial_cell", "urine_casts", "urine_bacteria",
            "urine_crystals", "urine_other"
        ],
        "영상 검사": [  # Imaging Tests
            "abdominal_sono", "thyroid_sono", "male_pelvis_sono", "chest_xray_ct",
            "carotid_artery_sono", "l_spine_ct", "c_spine_ct"
        ],
    }


def get_accordion_sections():
    groups = get_field_groups()
    return [
        {"title": "🧟 신체 측정", "id": "vitals", "color": "bg-light", "fields": groups["신체 측정"]},
        {"title": "👁️ 안과", "id": "eye", "color": "bg-danger-subtle", "fields": groups["안과"]},
        {"title": "🎧 청량", "id": "hearing", "color": "bg-danger-subtle", "fields": groups["청력"]},
        {"title": "💓 심전도", "id": "ekg", "color": "bg-danger-subtle", "fields": groups["심전도"]},
        {"title": "📷 내시경", "id": "endoscopy", "color": "bg-danger-subtle", "fields": groups["내시경"]},
        {"title": "🗅️ 영상검사", "id": "radiography", "color": "bg-danger-subtle", "fields": groups["영상 검사"]},
        {"title": "🍬 당뇨", "id": "diabetes", "color": "bg-light", "fields": groups["당뇨 검사"]},
        {"title": "🧪 간기능", "id": "liver", "color": "bg-warning-subtle", "fields": groups["간 기능"]},
        {"title": "🧬 신장·대사", "id": "kidney", "color": "bg-warning-subtle", "fields": groups["신장 및 대사"]},
        {"title": "🤔 전해질 및 비타민", "id": "electrolytes", "color": "bg-info-subtle", "fields": groups["전해질 및 비타민"]},
        {"title": "🧼 근육 효소", "id": "enzymes", "color": "bg-info-subtle", "fields": groups["근육 효소"]},
        {"title": "🚩 자율신경 및 스트레스", "id": "stress", "color": "bg-secondary-subtle", "fields": groups["자율신경 및 스트레스"]},
        {"title": "🦴 골다공증", "id": "bone", "color": "bg-secondary-subtle", "fields": groups["골다공증"]},
        {"title": "🧪 지질검사", "id": "lipid", "color": "bg-success-subtle", "fields": groups["지질"]},
        {"title": "🦠 감염질환", "id": "infection", "color": "bg-success-subtle", "fields": groups["감염 질환"]},
        {"title": "🩸 혈액검사", "id": "blood", "color": "bg-danger-subtle", "fields": groups["혈액 검사"]},
        {"title": "🧲 동풍·류마티스 및 염증", "id": "gout", "color": "bg-danger-subtle", "fields": groups["통풍 및 류마티스"]},
        {"title": "🦧 암표지자", "id": "cancer", "color": "bg-danger-subtle", "fields": groups["암 표지자"]},
        {"title": "🦤 갑상선", "id": "thyroid", "color": "bg-secondary-subtle", "fields": groups["갑상선"]},
        {"title": "💩 대변검사", "id": "stool", "color": "bg-info-subtle", "fields": groups["대변 검사"]},
        {"title": "💧 소변검사", "id": "urine", "color": "bg-info-subtle", "fields": groups["소변 검사"]},
        {"title": "📊 체성분", "id": "inbody", "color": "bg-info-subtle", "fields": groups["체성분"] + groups["부위별 근육량"]},
    ]

def get_field_labels():
    return {
        "date_measured": "측정일",
        "height": "키 (cm)",
        "weight": "몸무게 (kg)",
        "waist_line": "허리둘레 (cm)",
        "systolic_bp": "수축기 혈압 (Systolic BP)",
        "diastolic_bp": "이완기 혈압 (Diastolic BP)",
        "cholesterol_total": "총 콜레스테롤 (Total Cholesterol)",
        "cholesterol_ldl": "LDL 콜레스테롤",
        "cholesterol_hdl": "HDL 콜레스테롤",
        "triglyceride": "중성지방 (Triglycerides)",
        "glucose": "공복 혈당 (Glucose)",
        "bmi": "체질량지수 (BMI)",
        "ocular_tension_left": "안압 (좌, mmHg)",
        "ocular_tension_right": "안압 (우, mmHg)",
        "fundus": "안저 소견 (Fundus)",
        "hearing": "청력 소견 (Hearing)",
        "ekg":"심전도 (EKG)",
        "gastroscopy":"위내시경 소견",
        "abdominal_sono":"상복부 초음파 소견",
        "thyroid_sono":"갑상선 초음파 소견",
        "male_pelvis_sono":"남성하복부 초음파 소견",
        "chest_xray_ct":"흉부 촬영",
        "total_protein":"총 단백질 (g/dL)",
        "albumin":"알부민 (Albumin: g/dL)",
        "globulin":"글로불린 (Globulin: g/dL)",
        "t_bilirubin":"총 빌리루빈 (T.Bilirubin: mg/dL)",
        "d_bilirubin":"직접 빌리루빈 (D.Bilirubin: mg/dL)",
        "sgot_ast":"혈청GOT (SGOT(AST): U/L)",
        "sgpt_alt":"혈청GPT (SGPT(ALT): U/L)",
        "alk_phosphatase":"알칼리포스파타제 (Alk.phosphatase: U/L)",
        "ggtp":"감마GTP: U/L",
        "ag_ratio":"A/G 비율 (A/G Ratio)",
        "bilirubin_indirect":"간접 빌리루빈 (mg/dL)",
        "hbsag":"B형 간염 항원 (HBsAg(ECLIA): COI)",
        "hbsab":"B형 간염 항체 (HBsAb(ECLIA): IU/L)",
        "ldh":"젖산탈수소효소 (LDH: U/L)",
        "bun":"요소질소 (BUN: mg/dL)",
        "creatinine":"크레아티닌 (Creatinine: mg/dL)",
        "egfr":"신사구체여과율 (e-GFR: mL/min/1.73㎡)",
        "bc_ratio":"BUN/Cr 비율 (B/C ratio)",
        "rpr":"매독검사 (RPR)",
        "wbc":"백혈구수 (WBC: ×10³/μL)",
        "segment":"중성구백분율 (Segment: %)",
        "band":"간상구백분율 (Band: %)",
        "lymphocyte":"임파구백분율 (Lymphocyte: %)",
        "monocyte":"단구백분율 (Monocyte: %)",
        "eosinophil": "호산구백분율 (Eosinophil: %)",
        "basophil":"염기구백분율 (Basophil: %)",
        "nucleated_rbc":"유핵적혈구수 (Nucleated RBC: /100WBCs)",
        "blast":"골수아구 (Blast: %)",
        "promyelocyte":"전골수구수 (Promyelocyte: %)",
        "myelocyte":"골수구수 (Myelocyte: %)",
        "metamyelocyte":"후골수구수 (Metamyelocyte: %)",
        "rbc":"적혈구수 (RBC: ×10⁶/μL)",
        "hemoglobin":"혈색소 (Hemoglobin: g/dL)",
        "hct":"혈구용적치 (HCT: %)",
        "mcv":"평균적혈구용적 (MCV: fL)",
        "mch":"적혈구혈색소 (MCH: pg)",
        "mchc":"적혈구혈색농도 (MCHC: %)",
        "rdw":"적혈구분포폭 (RDW: %)",
        "platelet":"혈소판수 (Platelet: ×10³/μL)",
        "pct":"혈소판크리트 (PCT: %)",
        "mpv":"평균혈소판용적 (MPV: fL)",
        "pdw":"혈소판분포폭 (PDW :%)",
        "uric_acid":"요산 (Uric acid: mg/dL)",
        "ra_factor":"류마티스 인자 (RA factor: IU/mL)",
        "afp":"알파태아단백 (AFP(ECLIA): ng/mL)",
        "cea":"태아성암항원 (CEA: ng/mL)",
        "psa":"전립선특이항원 (PSA: ng/mL)",
        "ca199":"암항원 (CA 19-9: U/mL)",
        "tsh":"갑상선자극호르몬: (TSH: µIU/mL)",
        "free_t4":"갑상선 Free T4 (ng/dL)",
        "stool_occult_blood":"분변 잠혈 반응",
        "urine_color":"소변 색",
        "urine_sg":"소변 비중",
        "urine_ph":"소변 산도 (pH)",
        "urine_protein":"소변 단백",
        "urine_glucose":"소변 포도당",
        "urine_ketone": "소변 케톤체 (Ketone Bodies)",
        "urine_bilirubin":"소변 빌리루빈 (Bilirubin)",
        "urine_nitrite":"소변 아질산염 (Nitrite)",
        "urine_blood":"요잠혈 (Blood)",
        "urine_urobilinogen":"소변 우로빌리노겐 (Urobilinogen)",
        "urine_rbc":"소변 적혈구 (개/HPF)",
        "urine_wbc":"소변 백혈구 (개/HPF)",
        "urine_epithelial_cell":"소변 상피세포 (개/HPF)",
        "urine_casts":"소변 원주",
        "urine_bacteria":"소변 세균",
        "urine_crystals":"소변 결정체",
        "urine_other":"소변 기타",
        "body_water":"체수분 (L)",
        "body_protein":"단백질량 (kg)",
        "body_minerals":"무기질량 (kg)",
        "body_fat_mass":"체지방량 (kg)",
        "skeletal_muscle_mass":"골격근량 (kg)",
        "percent_body_fat":"체지방률 (%)",
        "ecw_ratio":"세포외수분비율 (ECW/TBW)",
        "right_arm":"오른팔 근육량 (kg)",
        "left_arm":"왼팔 근육량 (kg)",
        "trunk":"몸통 근육량 (kg)",
        "right_leg":"오른다리 근육량 (kg)",
        "left_leg":"왼다리 근육량 (kg)",
        "bone_density":"골밀도 (g/cm²)",
        "autonomic_nervous_balance":"자율신경 균형",
        "autonomic_nervous_activity":"자율신경 활동",
        "stress_index":"스트레스 지수",
        "ck_mb":"크레아틴 키나제 MB (CK-MB: U/L)",
        "sodium":"나트륨 (Sodium: mmol/L)",
        "potassium":"칼륨 (Potassium: mmol/L)",
        "chloride":"염화물 (Chloride: mmol/L)",
        "calcium":"칼슘 (Calcium: mg/dL)",
        "phosphorus":"인 (Phosphorus: mg/dL)",
        "c_reactive_protein":"C-반응성 단백 (CRP: mg/L)",
        "anti_hcv":"C형 간염 항체 (Anti-HCV: COI)",
        "hav_lgm":"A형 간염 IgM 항체 (HAV IgM: COI)",
        "hb_a1c":"당화혈색소 (HbA1c: %)",
        "carotid_artery_sono":"경동맥 초음파 소견",
        "l_spine_ct":"요추 CT 소견",
        "c_spine_ct":"경추 CT 소견",
        "vitamin_d":"비타민 D (25-OH Vitamin D: ng/mL)",
        "absolute_neutrophil_count":"절대 호중구 수 (ANC: /μL)",
        "absolute_lymphocyte_count":"절대 림프구 수 (ALC: /μL)",
        "absolute_monocyte_count":"절대 단핵구 수 (AMC: /μL)",
        "absolute_eosinophil_count":"절대 호산구 수 (AEC: /μL)",
        "absolute_basophil_count":"절대 호염기구 수 (ABC: /μL)",
        "immature_granulocyte":"미성숙 과립구 (IG: %)",
        "absolute_immature_granulocyte_count":"절대 미성숙 과립구 수 (AIGC: /μL)",
        "carbon_dioxide":"이산화탄소 (CO2: mmol/L)",
        "urine_wbc_esterase":"소변 백혈구 에스터레이스 (WBC Esterase)",
        "cholesterol_vldl":"VLDL 콜레스테롤 (mg/dL)",
        "vitamin_b12":"비타민 B12 (Vitamin B12: pg/mL)",
        "serum_folate":"혈청 엽산 (Serum Folate: ng/mL)",
    }

def model_to_dict_full(instance):
    data = model_to_dict(instance)
    data['date_measured'] = instance.date_measured.isoformat()
    return data