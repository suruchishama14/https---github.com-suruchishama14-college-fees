from django.db import models

# Create your models here.
CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

CHOICE_YEAR = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)

CHOICES_OPTED = (
    ("Yes", 'Yes'),
    ("No", 'No'),
)


class StudentDetailsCommon(models.Model):
    student_name = models.CharField(max_length=100, verbose_name='Student Name')
    fathers_name = models.CharField(max_length=100, verbose_name="Father's Name")
    dob = models.DateField(verbose_name='Date of Birth')
    gender = models.CharField(max_length=30, choices=CHOICES, verbose_name='Gender')
    session_of_add = models.CharField(max_length=301, verbose_name='Session')
    course_duration = models.CharField(max_length=10, choices=CHOICE_YEAR, verbose_name='Course Duration')
    course = models.CharField(max_length=30, verbose_name='Course')
    branch = models.CharField(max_length=30, verbose_name='Branch')
    contact = models.IntegerField(verbose_name="Parent's contact")
    email = models.EmailField(max_length=100, verbose_name='Email')
    bus = models.CharField(max_length=30, choices=CHOICES_OPTED, verbose_name='Bus Service')
    hostel = models.CharField(max_length=30, choices=CHOICES_OPTED, verbose_name='Hostel')
    mess = models.CharField(max_length=30, choices=CHOICES_OPTED, verbose_name='Mess')
    clinic = models.CharField(max_length=30, choices=CHOICES_OPTED, verbose_name='clinical')

    class Meta:
        abstract = True


class FirstYearFee(models.Model):
    f_tuition_fee = models.FloatField(verbose_name='First Year Tuition Fees')
    f_development_fee = models.FloatField(verbose_name='First Year Development Fees')
    # Other Fees
    admission_fee = models.FloatField()
    f_lab_computer_fee = models.FloatField(verbose_name='First Year Lab, Computer & A/V Aids Fees')
    f_library = models.FloatField(verbose_name='First Year Library & Magazine ')
    f_sports_activities = models.FloatField(verbose_name='First Year Sports & Extracurricular activities ')
    f_college_exam = models.FloatField(verbose_name='First Year College Exam Fees')
    f_student_welfare = models.FloatField(verbose_name='First Year Student’s Welfare')
    # Hostel and transportation
    f_bus_fees = models.FloatField(verbose_name='First Year Conveyance for Clinical (Bus)', default=0)
    f_hostel_fees = models.FloatField(verbose_name='First Year Hostel Fees', default=0)
    f_mess_fees = models.FloatField(verbose_name='First Year Mess Fees', default=0)
    f_clinic_fees = models.FloatField(verbose_name='First Year Clinical fee', default=0)
    # Non Academic
    caution_fee = models.FloatField(verbose_name='Caution Deposit (To be refunded on completion of course)')
    clerical_fee = models.FloatField(verbose_name='CLERICAL FEE')
    med_equip = models.FloatField(verbose_name='MED.EQP')
    uniform_fee = models.FloatField()
    wel_kit = models.FloatField()
    prac_rec = models.FloatField()

    class Meta:
        abstract = True


class SecondYearFee(models.Model):
    s_tuition_fee = models.FloatField(verbose_name='Second Year Tuition Fees')
    s_development_fee = models.FloatField(verbose_name='Second Year Development Fees')
    # Other Fees
    s_lab_computer_fee = models.FloatField(verbose_name='Second Year Lab, Computer & A/V Aids Fees')
    s_library = models.FloatField(verbose_name='Second Year Library & Magazine ')
    s_sports_activities = models.FloatField(verbose_name='Second Year Sports & Extracurricular activities ')
    s_college_exam = models.FloatField(verbose_name='Second Year College Exam Fees')
    s_student_welfare = models.FloatField(verbose_name='Second Year Student’s Welfare')
    # Hostel and transportation
    s_bus_fees = models.FloatField(verbose_name='Second Year Conveyance for Clinical (Bus)', default=0)
    s_hostel_fees = models.FloatField(verbose_name='Second Year Hostel Fees', default=0)
    s_mess_fees = models.FloatField(verbose_name='Second Year Mess Fees', default=0)
    s_clinic_fees = models.FloatField(verbose_name='Second Year Clinical Fee', default=0)

    class Meta:
        abstract = True


class ThirdYearFee(models.Model):
    t_tuition_fee = models.FloatField(verbose_name='Third Year Tuition Fees')
    t_development_fee = models.FloatField(verbose_name='Third Year Development Fees')
    # Other Fees
    t_lab_computer_fee = models.FloatField(verbose_name='Third Year Lab, Computer & A/V Aids Fees')
    t_library = models.FloatField(verbose_name='Third Year Library & Magazine ')
    t_sports_activities = models.FloatField(verbose_name='Third Year Sports & Extracurricular activities ')
    t_college_exam = models.FloatField(verbose_name='Third Year College Exam Fees')
    t_student_welfare = models.FloatField(verbose_name='Third Year Student’s Welfare')
    # Hostel and transportation
    t_bus_fees = models.FloatField(verbose_name='Third Year Conveyance for Clinical (Bus)', default=0)
    t_hostel_fees = models.FloatField(verbose_name='Third Year Hostel Fees', default=0)
    t_mess_fees = models.FloatField(verbose_name='Third Year Mess Fees', default=0)
    t_clinic_fees = models.FloatField(verbose_name='Third Year Clinical Fee', default=0)

    class Meta:
        abstract = True


class FourthYearFee(models.Model):
    fo_tuition_fee = models.FloatField(verbose_name='Fourth Year Tuition Fees')
    fo_development_fee = models.FloatField(verbose_name='Fourth Year Development Fees')
    # Other Fees
    fo_lab_computer_fee = models.FloatField(verbose_name='Fourth Year Lab, Computer & A/V Aids Fees')
    fo_library = models.FloatField(verbose_name='Fourth Year Library & Magazine ')
    fo_sports_activities = models.FloatField(verbose_name='Fourth Year Sports & Extracurricular activities ')
    fo_college_exam = models.FloatField(verbose_name='Fourth Year College Exam Fees')
    fo_student_welfare = models.FloatField(verbose_name='Fourth Year Student’s Welfare')
    # Hostel and transportation
    fo_bus_fees = models.FloatField(verbose_name='Fourth Year Conveyance for Clinical (Bus)', default=0)
    fo_hostel_fees = models.FloatField(verbose_name='Fourth Year Hostel Fees', default=0)
    fo_mess_fees = models.FloatField(verbose_name='Fourth Year Mess Fees', default=0)
    fo_clinic_fees = models.FloatField(verbose_name='Fourth Year Clinical Fee', default=0)

    class Meta:
        abstract = True


class FirstYr(FirstYearFee):
    f_actual_fees = models.FloatField(max_length=20, verbose_name='First Year Actual Amount')
    f_concession = models.FloatField(max_length=30, verbose_name='Concession')
    f_balance = models.FloatField(max_length=20, verbose_name='First year Balance')
    f_currently_paid = models.FloatField(max_length=20, verbose_name='Currently Paid')
    f_net_pay = models.FloatField(max_length=20, verbose_name='Net Payable of First Year Fees')

    class Meta:
        abstract = True


class SecondYr(SecondYearFee):
    s_actual_fees = models.FloatField(max_length=20, verbose_name='Second Year Actual Amount')
    s_concession = models.FloatField(max_length=30, verbose_name='Concession')
    s_balance = models.FloatField(max_length=20, verbose_name='Second year Balance')
    s_currently_paid = models.FloatField(max_length=20, verbose_name='Currently Paid')
    s_net_pay = models.FloatField(max_length=20, verbose_name='Net Payable of Second Year Fees')

    class Meta:
        abstract = True


class ThirdYr(ThirdYearFee):
    t_actual_fees = models.FloatField(max_length=20, verbose_name='Third Year Actual Amount')
    t_concession = models.FloatField(max_length=30, verbose_name='Concession')
    t_balance = models.FloatField(max_length=20, verbose_name='Third year Balance')
    t_currently_paid = models.FloatField(max_length=20, verbose_name='Currently Paid')
    t_net_pay = models.FloatField(max_length=20, verbose_name='Net Payable of Third Year Fees')

    class Meta:
        abstract = True


class FourthYr(FourthYearFee):
    fo_actual_fees = models.FloatField(max_length=20, verbose_name='Fourth Year Actual Amount')
    fo_concession = models.FloatField(max_length=30, verbose_name='Concession')
    fo_balance = models.FloatField(max_length=20, verbose_name='Fourth year Balance')
    fo_currently_paid = models.FloatField(max_length=20, verbose_name='Currently Paid')
    fo_net_pay = models.FloatField(max_length=20, verbose_name='Net Payable of Fourth Year Fees')

    class Meta:
        abstract = True


class StudentFeeDetails(StudentDetailsCommon, FirstYr, SecondYr, ThirdYr, FourthYr):
    def __str__(self):
        return self.student_name

    class Meta:
        db_table = 'Student Database'
        verbose_name = 'Student Database'


TYPE_OF_FEES = (
    ("Fees", "Fees"),
    ("Fine", "Fine"),
    ("Hostel", "Hostel"),
    ("Hostel & Mess", "Hostel & Mess"),
    ("Bus Service", "Bus Service"),
)


# Fees Transaction database


class FeesTransaction(models.Model):
    student_name = models.CharField(max_length=100, verbose_name='Student Name')
    fathers_name = models.CharField(max_length=100, verbose_name="Father's Name")
    year = models.CharField(max_length=30, choices=CHOICE_YEAR, verbose_name='Year')
    email = models.EmailField(max_length=50, verbose_name='Email')
    fee_type = models.CharField(max_length=30, choices=TYPE_OF_FEES, verbose_name='Type')
    fees_amount = models.FloatField(max_length=10, verbose_name='Amount')
    dos = models.DateTimeField(auto_now=True, verbose_name='Date')

    def __str__(self):
        return self.student_name

    def year_module(self):
        return self.dos.year

    class Meta:
        db_table = 'Fees Transaction'
        verbose_name = 'Fees Transaction'

# Fees Details Session Wise


class FeesDetailsSessionWise(FirstYearFee, SecondYearFee, ThirdYearFee, FourthYearFee):
    Session = models.CharField(max_length=100, verbose_name='session')
    date = models.DateField(verbose_name='Date of fee structure')

    def __str__(self):
        return self.Session

    class Meta:
        db_table = 'Fees Details Session Wise'
        verbose_name = 'Fees Details Session wise'
