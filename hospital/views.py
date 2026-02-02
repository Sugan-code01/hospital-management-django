
from django.shortcuts import render, redirect
from .models import Patient, Doctor, Appointment

def home(request):
    return render(request,'home.html')

def add_patient(request):
    if request.method=='POST':
        Patient.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            gender=request.POST['gender']
        )
        return redirect('patients')
    return render(request,'add_patient.html')

def patients(request):
    q = request.GET.get('q','')
    patients = Patient.objects.filter(name__icontains=q)
    return render(request,'patients.html',{'patients':patients,'q':q})

def update_patient(request,id):
    p = Patient.objects.get(id=id)
    if request.method=='POST':
        p.name=request.POST['name']
        p.age=request.POST['age']
        p.gender=request.POST['gender']
        p.save()
        return redirect('patients')
    return render(request,'update_patient.html',{'p':p})

def delete_patient(request,id):
    Patient.objects.get(id=id).delete()
    return redirect('patients')

def add_doctor(request):
    if request.method=='POST':
        Doctor.objects.create(
            name=request.POST['name'],
            specialization=request.POST['specialization']
        )
        return redirect('doctors')
    return render(request,'add_doctor.html')

def doctors(request):
    return render(request,'doctors.html',{'doctors':Doctor.objects.all()})

def add_appointment(request):
    if request.method=='POST':
        Appointment.objects.create(
            patient_id=request.POST['patient'],
            doctor_id=request.POST['doctor'],
            date=request.POST['date']
        )
        return redirect('home')
    return render(request,'add_appointment.html',{
        'patients':Patient.objects.all(),
        'doctors':Doctor.objects.all()
    })
