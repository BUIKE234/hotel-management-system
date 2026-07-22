
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking, RoomType
from .forms import BookingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')


def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            check_in = form.cleaned_data['check_in_date']
            check_out = form.cleaned_data['check_out_date']
            if check_out <= check_in:
                messages.error(request, "Check-out date must be after Check-in date")
            else:
                form.save()
                messages.success(request, "Room booked successfully! We will contact you soon.")
                return redirect('success')
    else:
        form = BookingForm()

    return render(request, 'book.html', {'form': form})


def rooms(request):
    room_types = RoomType.objects.all()
    return render(request, 'rooms.html', {'room_types': room_types})


def about(request):
    return render(request, 'About.html')


def bookings(request):
    booking_list = Booking.objects.select_related('room_type').order_by('-booked_at')
    return render(request, 'bookings.html', {'bookings': booking_list})


def contacts(request):
    return render(request, 'contacts.html')


def success(request):
    return render(request, 'success.html')


def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_success', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})


def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'success.html', {'booking': booking})
