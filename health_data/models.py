from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class HealthRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_measured = models.DateField()

    # Basic Vitals
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    waist_line = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    bmi = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, editable=False)
    systolic_bp = models.IntegerField(null=True, blank=True)
    diastolic_bp = models.IntegerField(null=True, blank=True)


    # Vision
    ocular_tension_left = models.IntegerField(null=True, blank=True)
    ocular_tension_right = models.IntegerField(null=True, blank=True)
    fundus = models.CharField(max_length=255, null=True, blank=True)

    # Hearing
    hearing = models.CharField(max_length=255, null=True, blank=True)

    # EKG
    ekg = models.CharField(max_length=255, null=True, blank=True)

    # Imaging
    gastroscopy = models.TextField(null=True, blank=True)
    abdominal_sono = models.TextField(null=True, blank=True)
    thyroid_sono = models.TextField(null=True, blank=True)
    male_pelvis_sono = models.TextField(null=True, blank=True)
    chest_xray_ct = models.TextField(null=True, blank=True)

    # Diabetes
    glucose = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # Liver Panel
    total_protein = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    albumin = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    globulin = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    t_bilirubin = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    d_bilirubin = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    sgpt_alt = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    sgot_ast = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    alk_phosphatase = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ggtp = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ag_ratio = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    bilirubin_indirect = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    hbsag = models.CharField(max_length=100, null=True, blank=True)
    hbsab = models.CharField(max_length=100, null=True, blank=True)

    # Kidney and metabolic
    ldh = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    bun = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    creatinine = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    egfr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    bc_ratio = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # Lipids
    cholesterol_total = models.IntegerField(null=True, blank=True)
    cholesterol_ldl = models.IntegerField(null=True, blank=True)
    cholesterol_hdl = models.IntegerField(null=True, blank=True)
    triglyceride = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # Other Infectious Diseases
    rpr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # Hematology
    wbc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    segment = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    band = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    lymphocyte = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    monocyte = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    eosinophil = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    basophil = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    nucleated_rbc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    blast = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    promyelocyte = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    myelocyte = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    metamyelocyte = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rbc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    hemoglobin = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    hct = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    mcv = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    mch = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    mchc = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rdw = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    platelet = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pct = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    mpv = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    pdw = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # Gout & Rheumatoid Arthritis
    uric_acid = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ra_factor = models.CharField(max_length=100, null=True, blank=True)


    # Cancer Markers
    afp = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cea = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    psa = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ca199 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # Thyroid
    tsh = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    free_t4 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # Stool test
    stool_occult_blood = models.CharField(max_length=100, null=True, blank=True)

    # Urinalysis
    urine_color = models.CharField(max_length=50, null=True, blank=True)
    urine_sg = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    urine_ph = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    urine_protein = models.CharField(max_length=50, null=True, blank=True)
    urine_glucose = models.CharField(max_length=50, null=True, blank=True)
    urine_ketone = models.CharField(max_length=50, null=True, blank=True)
    urine_bilirubin = models.CharField(max_length=50, null=True, blank=True)
    urine_nitrite = models.CharField(max_length=50, null=True, blank=True)
    urine_blood = models.CharField(max_length=50, null=True, blank=True)
    urine_urobilinogen = models.CharField(max_length=50, null=True, blank=True)
    urine_rbc = models.CharField(max_length=50, null=True, blank=True)
    urine_wbc = models.CharField(max_length=50, null=True, blank=True)
    urine_epithelial_cell = models.CharField(max_length=50, null=True, blank=True)
    urine_casts = models.CharField(max_length=50, null=True, blank=True)
    urine_bacteria = models.CharField(max_length=50, null=True, blank=True)
    urine_crystals = models.CharField(max_length=50, null=True, blank=True)
    urine_other = models.CharField(max_length=50, null=True, blank=True)

    # InBody composition
    body_water = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    body_protein = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    body_minerals = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    body_fat_mass = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    skeletal_muscle_mass = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    percent_body_fat = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    ecw_ratio = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)

    # Segmental lean analysis
    right_arm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    left_arm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    trunk = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    right_leg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    left_leg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        try:
            if self.weight and self.height and self.height > 0:
                height_in_m = self.height / Decimal('100')  # convert cm to m
                self.bmi = self.weight / (height_in_m ** 2)
        except (InvalidOperation, ZeroDivisionError):
            self.bmi = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.date_measured}"
