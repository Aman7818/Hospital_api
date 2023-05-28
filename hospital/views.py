from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor, Patient, Report
from .authentication import generate_jwt_token

@api_view(['POST'])
def doctor_register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    doctor = Doctor(username=username, password=password)
    doctor.save()

    return Response({'message': 'Doctor registered successfully.'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def doctor_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        doctor = Doctor.objects.get(username=username, password=password)
    except Doctor.DoesNotExist:
        return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)

    token = generate_jwt_token(doctor)
    return Response({'token': token}, status=status.HTTP_200_OK)

@api_view(['POST'])
def patient_register(request):
    phone_number = request.data.get('phone_number')

    if not phone_number:
        return Response({'error': 'Phone number is required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        patient = Patient.objects.get(phone_number=phone_number)
        return Response({'patient_id': patient.id, 'message': 'Patient already exists.'}, status=status.HTTP_200_OK)
    except Patient.DoesNotExist:
        patient = Patient(phone_number=phone_number)
        patient.save()
        return Response({'patient_id': patient.id, 'message': 'Patient registered successfully.'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def create_report(request, id):
    doctor_id = request.data.get('doctor_id')
    status = request.data.get('status')

    if not doctor_id or not status:
        return Response({'error': 'Doctor ID and status are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except Doctor.DoesNotExist:
        return Response({'error': 'Doctor does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        patient = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return Response({'error': 'Patient does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    report = Report(doctor=doctor, patient=patient, status=status)
    report.save()

    return Response({'report_id': report.id, 'message': 'Report created successfully.'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def all_reports(request, id):
    try:
        patient = Patient.objects.get(id=id)
    except Patient.DoesNotExist:
        return Response({'error': 'Patient does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    reports = Report.objects.filter(patient=patient).order_by('date')
    report_list = []

    for report in reports:
        report_list.append({
            'id': report.id,
            'created_by': report.doctor.username,
            'status': report.status,
            'date': report.date
        })

    return Response({'reports': report_list}, status=status.HTTP_200_OK)

@api_view(['GET'])
def reports_by_status(request, status):
    reports = Report.objects.filter(status=status)
    report_list = []

    for report in reports:
        report_list.append({
            'id': report.id,
            'created_by': report.doctor.username,
            'status': report.status,
            'date': report.date
        })

    return Response({'reports': report_list}, status=status.HTTP_200_OK)
