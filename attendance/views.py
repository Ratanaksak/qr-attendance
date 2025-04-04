from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendee, AttendanceRecord
from django.contrib.auth.models import User
from django.http import JsonResponse
import uuid

@login_required
def dashboard(request):
    try:
        attendee = Attendee.objects.get(user=request.user)
    except Attendee.DoesNotExist:
        attendee = Attendee.objects.create(user=request.user)
    return render(request, 'attendance/dashboard.html', {'attendee': attendee})

@login_required
def scan_qr(request):
    if request.method == 'POST':
        qr_data = request.POST.get('qr_data')
        try:
            attendee = Attendee.objects.get(unique_id=qr_data)
            AttendanceRecord.objects.create(attendee=attendee)
            return JsonResponse({'status': 'success', 'name': attendee.user.username})
        except Attendee.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Invalid QR code'})
    return render(request, 'attendance/scan.html')

@login_required
def attendance_records(request):
    attendee = Attendee.objects.get(user=request.user)
    records = AttendanceRecord.objects.filter(attendee=attendee)
    return render(request, 'attendance/records.html', {'records': records})