
from django.shortcuts import render
from students.models import Student
from django.db.models import Q




#  LOGIC FOR ALL STUDENTS
def college_all_students(request):
    all_students = Student.objects.all()
    context = {
        'all_students' : all_students,
    }
    return render(request , 'all_year_student.html', context)









# LOGIC FOR CSM STUDENT
def csm_4th_years(request):
    csm_year_4th = Student.objects.order_by('registration_id').filter(studying_year='4th Year', section='CSM')
    student_count = csm_year_4th.count()
    context = {
        'csm_year_4th': csm_year_4th,
        'student_count' : student_count,
    }
    return render(request,'CSM/csm_4th_year.html', context)

def csm_3rd_years(request):
    csm_year_3rd = Student.objects.order_by('registration_id').filter(studying_year='3rd Year', section='CSM')
    student_count = csm_year_3rd.count()
    
    context = {
        'csm_year_3rd': csm_year_3rd,
        'student_count' : student_count,
    }
    return render(request,'CSM/csm_3rd_year.html', context)

def csm_2nd_years(request):
    csm_year_2nd = Student.objects.order_by('registration_id').filter(studying_year='2nd Year', section='CSM')
    student_count = csm_year_2nd.count()
    context = {
        'csm_year_2nd': csm_year_2nd,
        'student_count' : student_count,
    }
    return render(request,'CSM/csm_2nd_year.html', context)

def csm_1st_years(request):
    csm_year_1st = Student.objects.order_by('registration_id').filter(studying_year='1st Year', section='CSM')
    student_count = csm_year_1st.count()
    context = {
        'csm_year_1st': csm_year_1st,
        'student_count' : student_count,
    }
    return render(request,'CSM/csm_1st_year.html', context)








# LOGIC FOR CSD STUDENTS
def csd_4th_years(request):
    csd_year_4th = Student.objects.order_by('registration_id').filter(studying_year='4th Year', section='CSD')
    student_count = csd_year_4th.count()
    context = {
        'csd_year_4th': csd_year_4th,
        'student_count' : student_count,
    }
    return render(request,'CSD/csd_4th_year.html', context)



def csd_3rd_years(request):
    csd_year_3rd = Student.objects.order_by('registration_id').filter(studying_year='3rd Year', section='CSD')
    student_count = csd_year_3rd.count()
    context = {
        'csd_year_3rd': csd_year_3rd,
        'student_count' : student_count,
    }
    return render(request,'CSD/csd_3rd_year.html', context)



def csd_2nd_years(request):
    csd_year_2nd = Student.objects.order_by('registration_id').filter(studying_year='2nd Year', section='CSD')
    student_count = csd_year_2nd.count()
    context = {
        'csd_year_2nd': csd_year_2nd,
        'student_count' : student_count,
    }
    return render(request,'CSD/csd_2nd_year.html', context)



def csd_1st_years(request):
    csd_year_1st = Student.objects.order_by('registration_id').filter(studying_year='1st Year', section='CSD')
    student_count = csd_year_1st.count()
    context = {
        'csd_year_1st': csd_year_1st,
        'student_count' : student_count,
    }
    return render(request,'CSD/csd_1st_year.html', context)








# LOGIC FOR CSC STUDENTS
def csc_4th_years(request):
    csc_year_4th = Student.objects.order_by('registration_id').filter(studying_year='4th Year', section='CSC')
    student_count = csc_year_4th.count()
    context = {
        'csc_year_4th': csc_year_4th,
        'student_count' : student_count,
    }
    return render(request,'CSC/csc_4th_year.html', context)



def csc_3rd_years(request):
    csc_year_3rd = Student.objects.order_by('registration_id').filter(studying_year='3rd Year', section='CSC')
    student_count = csc_year_3rd.count()
    context = {
        'csc_year_3rd': csc_year_3rd,
        'student_count' : student_count,
    }
    return render(request,'CSC/csc_3rd_year.html', context)



def csc_2nd_years(request):
    csc_year_2nd = Student.objects.order_by('registration_id').filter(studying_year='2nd Year', section='CSC')
    student_count = csc_year_2nd.count()
    context = {
        'csc_year_2nd': csc_year_2nd,
        'student_count' : student_count,
    }
    return render(request,'CSC/csc_2nd_year.html', context)



def csc_1st_years(request):
    csc_year_1st = Student.objects.order_by('registration_id').filter(studying_year='1st Year', section='CSC')
    student_count = csc_year_1st.count()
    context = {
        'csc_year_1st': csc_year_1st,
        'student_count' : student_count,
    }
    return render(request,'CSC/csc_1st_year.html', context)








# LOGIC FOR CSE STUDENTS
def cse_4th_years(request):
    cse_year_4th = Student.objects.order_by('registration_id').filter(studying_year='4th Year', section='CSE')
    student_count = cse_year_4th.count()
    context = {
        'cse_year_4th': cse_year_4th,
        'student_count' : student_count,
    }
    return render(request,'CSE/cse_4th_year.html', context)



def cse_3rd_years(request):
    cse_year_3rd = Student.objects.order_by('registration_id').filter(studying_year='3rd Year', section='CSE')
    student_count = cse_year_3rd.count()
    context = {
        'cse_year_3rd': cse_year_3rd,
        'student_count' : student_count,
    }
    return render(request,'CSE/cse_3rd_year.html', context)



def cse_2nd_years(request):
    cse_year_2nd = Student.objects.order_by('registration_id').filter(studying_year='2nd Year', section='CSE')
    student_count = cse_year_2nd.count()
    context = {
        'cse_year_2nd': cse_year_2nd,
        'student_count' : student_count,
    }
    return render(request,'CSE/cse_2nd_year.html', context)



def cse_1st_years(request):
    cse_year_1st = Student.objects.order_by('registration_id').filter(studying_year='1st Year', section='CSE')
    student_count = cse_year_1st.count()
    context = {
        'cse_year_1st': cse_year_1st,
        'student_count' : student_count,
    }
    return render(request,'CSE/cse_1st_year.html', context)











# LOGIC FOE MECHANICAL STUDENTS
def mech_4th_years(request):
    mech_year_4th = Student.objects.order_by('registration_id').filter(studying_year='4th Year', section='MECH')
    student_count = mech_year_4th.count()
    context = {
        'mech_year_4th': mech_year_4th,
        'student_count' : student_count,
    }
    return render(request,'MECH/mech_4th_year.html', context)



def mech_3rd_years(request):
    mech_year_3rd = Student.objects.order_by('registration_id').filter(studying_year='3rd Year', section='MECH')
    student_count = mech_year_3rd.count()
    context = {
        'mech_year_3rd': mech_year_3rd,
        'student_count' : student_count,
    }
    return render(request,'MECH/mech_3rd_year.html', context)



def mech_2nd_years(request):
    mech_year_2nd = Student.objects.order_by('registration_id').filter(studying_year='2nd Year', section='MECH')
    student_count = mech_year_2nd.count()
    context = {
        'mech_year_2nd': mech_year_2nd,
        'student_count' : student_count,
    }
    return render(request,'MECH/mech_2nd_year.html', context)



def mech_1st_years(request):
    mech_year_1st = Student.objects.order_by('registration_id').filter(studying_year='1st Year', section='MECH')
    student_count = mech_year_1st.count()
    context = {
        'mech_year_1st': mech_year_1st,
        'student_count' : student_count,
    }
    return render(request,'MECH/mech_1st_year.html', context)













# LOGIC FOR CIVIL STUDENTS
def civil_4th_years(request):
    civil_year_4th = Student.objects.order_by('registration_id').filter(studying_year='4th Year', section='CIVIL')
    student_count = civil_year_4th.count()
    context = {
        'civil_year_4th': civil_year_4th,
        'student_count' : student_count,
    }
    return render(request,'CIVIL/civil_4th_year.html', context)



def civil_3rd_years(request):
    civil_year_3rd = Student.objects.order_by('registration_id').filter(studying_year='3rd Year', section='CIVIL')
    student_count = civil_year_3rd.count()
    context = {
        'civil_year_3rd': civil_year_3rd,
        'student_count' : student_count,
    }
    return render(request,'CIVIL/civil_3rd_year.html', context)



def civil_2nd_years(request):
    civil_year_2nd = Student.objects.order_by('registration_id').filter(studying_year='2nd Year', section='CIVIL')
    student_count = civil_year_2nd.count()
    context = {
        'civil_year_2nd': civil_year_2nd,
        'student_count' : student_count,
    }
    return render(request,'CIVIL/civil_2nd_year.html', context)



def civil_1st_years(request):
    civil_year_1st = Student.objects.order_by('registration_id').filter(studying_year='1st Year', section='CIVIL')
    student_count = civil_year_1st.count()
    context = {
        'civil_year_1st': civil_year_1st,
        'student_count' : student_count,
    }
    return render(request,'CIVIL/civil_1st_year.html', context)











# LOGIC FOR ECE STUDENTS
def ece_4th_years(request):
    ece_year_4th = Student.objects.order_by('registration_id').filter(studying_year='4th Year', section='ECE')
    student_count = ece_year_4th.count()
    context = {
        'ece_year_4th': ece_year_4th,
        'student_count' : student_count,
    }
    return render(request,'ECE/ece_4th_year.html', context)



def ece_3rd_years(request):
    ece_year_3rd = Student.objects.order_by('registration_id').filter(studying_year='3rd Year', section='ECE')
    student_count = ece_year_3rd.count()
    context = {
        'ece_year_3rd': ece_year_3rd,
        'student_count' : student_count,
    }
    return render(request,'ECE/ece_3rd_year.html', context)



def ece_2nd_years(request):
    ece_year_2nd = Student.objects.order_by('registration_id').filter(studying_year='2nd Year', section='ECE')
    student_count = ece_year_2nd.count()
    context = {
        'ece_year_2nd': ece_year_2nd,
        'student_count' : student_count,
    }
    return render(request,'ECE/ece_2nd_year.html', context)



def ece_1st_years(request):
    ece_year_1st = Student.objects.order_by('registration_id').filter(studying_year='1st Year', section='ECE')
    student_count = ece_year_1st.count()
    context = {
        'ece_year_1st': ece_year_1st,
        'student_count' : student_count,
    }
    return render(request,'ECE/ece_1st_year.html', context)












# LOGIC FOR EEE STUDENTS
def eee_4th_years(request):
    eee_year_4th = Student.objects.order_by('registration_id').filter(studying_year='4th Year', section='EEE')
    student_count = eee_year_4th.count()
    context = {
        'eee_year_4th': eee_year_4th,
        'student_count' : student_count,
    }
    return render(request,'EEE/eee_4th_year.html', context)



def eee_3rd_years(request):
    eee_year_3rd = Student.objects.order_by('registration_id').filter(studying_year='3rd Year', section='EEE')
    student_count = eee_year_3rd.count()
    context = {
        'eee_year_3rd': eee_year_3rd,
        'student_count' : student_count,
    }
    return render(request,'EEE/eee_3rd_year.html', context)



def eee_2nd_years(request):
    eee_year_2nd = Student.objects.order_by('registration_id').filter(studying_year='2nd Year', section='EEE')
    student_count = eee_year_2nd.count()
    context = {
        'eee_year_2nd': eee_year_2nd,
        'student_count' : student_count,
    }
    return render(request,'EEE/eee_2nd_year.html', context)



def eee_1st_years(request):
    eee_year_1st = Student.objects.order_by('registration_id').filter(studying_year='1st Year', section='EEE')
    student_count = eee_year_1st.count()
    context = {
        'eee_year_1st': eee_year_1st,
        'student_count' : student_count,
    }
    return render(request,'EEE/eee_1st_year.html', context)







def search(request):
    students = Student.objects.order_by('registration_id')
    student_count = students.count()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            students = Student.objects.order_by('-studying_year').filter(Q(registration_id__icontains = keyword) |  Q(first_name__icontains=keyword) |  Q(last_name__icontains=keyword))
            student_count = students.count()
        
        
    context = {
        'students': students,
        'student_count' : student_count,
    }
    return render(request , 'all_year_student.html',context)











def home(request):
    return render(request,'home.html')