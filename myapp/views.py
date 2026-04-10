from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def why_choose_us(request):
    return render(request, 'why_choose_us.html')

def car_software_repair_and_programming(request):
    return render(request, 'car_software_repair_and_programming.html')

def comfort_system_repair(request):
    return render(request, 'comfort_system_repair.html')


def engine_control_unit_repair(request):
    return render(request, 'engine_control_unit_repair.html')


def touchless_wheel_alignment(request):
    return render(request, 'touchless_wheel_alignment.html')


def transmission_repair(request):
    return render(request, 'transmission_repair.html')


def fleet_maintenance(request):
    return render(request, 'fleet_maintenance.html')

def body_and_repair_service(request):
    return render(request, 'body_and_repair_service.html')

def car_facelift(request):
    return render(request, 'car_facelift.html')

def car_insurance(request):
    return render(request, 'car_insurance.html')

def electric_car_repair(request):
    return render(request, 'electric_car_repair.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def tinting(request):
    return render(request, 'tinting.html')

def suspension(request):
    return render(request, 'suspension.html')

def software(request):
    return render(request, 'software.html')

def reviews(request):
    return render(request, 'reviews.html')

def ppf(request):
    return render(request, 'ppf.html')

def navigation(request):
    return render(request, 'navigation.html')

def minor(request):
    return render(request, 'minor.html')

def management(request):
    return render(request, 'management.html')

def major(request):
    return render(request, 'major.html')

def inspection(request):
    return render(request, 'inspection.html')

def gearbox(request):
    return render(request, 'gearbox.html')

def gallery(request):
    return render(request, 'gallery.html')

def dip(request):
    return render(request, 'dip.html')

def detailing(request):
    return render(request, 'detailing.html')

def cooling(request):
    return render(request, 'cooling.html')

def ceramic(request):
    return render(request, 'ceramic.html')

def camera(request):
    return render(request, 'camera.html')

def caliper(request):
    return render(request, 'caliper.html')

def brake(request):
    return render(request, 'brake.html')

def axle(request):
    return render(request, 'axle.html')

def ac(request):
    return render(request, 'ac.html')


def packages(request):
    return render(request, 'packages.html')




def appointment_success(request):
    return render(request, 'appointment_success.html')



from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import AppointmentForm
from .forms import ContactForm
from django.contrib import messages


def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()

            
            admin_subject = 'New Appointment Booking'
            admin_message = f"New Appointment Details:\n\nName: {appointment.name}\nEmail: {appointment.email}\nService: {appointment.service}\nDate: {appointment.service_date}"
            
            send_mail(
                admin_subject,
                admin_message,
                settings.DEFAULT_FROM_EMAIL,
                ['ardrapb201@gmail.com'],
                fail_silently=True,
            )

           
            customer_subject = 'Appointment Confirmation - Elegant Way Auto Maint'
            customer_message = f"Hi {appointment.name},\n\nThank you for booking with Elegant Way Auto Maint. We have received your request for {appointment.service} on {appointment.service_date}. Our team will contact you shortly to confirm the timing.\n\nBest Regards,\nElegant Way Team"
            
            send_mail(
                customer_subject,
                customer_message,
                settings.DEFAULT_FROM_EMAIL,
                [appointment.email],
                fail_silently=True,
            )

            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'reviews.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_obj = form.save()

            # 📩 Email to admin
            send_mail(
                'New Contact Inquiry',
                f"New Inquiry:\n\nName: {contact_obj.name}\nEmail: {contact_obj.email}\nMessage: {contact_obj.message}",
                settings.DEFAULT_FROM_EMAIL,
                ['ardrapb201@gmail.com'],
                fail_silently=False,  # 👈 show errors if email fails
            )

            # 📩 Auto-reply to customer
            send_mail(
                'We received your message!',
                f"Hi {contact_obj.name},\n\n"
                f"Thanks for reaching out! We've received your message and our team will contact you shortly.\n\n"
                f"Best Regards,\nElegant Way Auto Maint",
                settings.DEFAULT_FROM_EMAIL,
                [contact_obj.email],
                fail_silently=False,
            )

            # ✅ Toast message trigger
            messages.success(request, "✅ Message sent successfully! We will contact you soon.")

            return redirect('contact')  # 👈 stay on same page (toast will show)

        else:
            # ❌ If form invalid
            messages.error(request, "❌ Something went wrong. Please check your inputs.")

    return render(request, 'contact.html', {'form': ContactForm()})






from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def review_page(request):
    # 1. Handle the POST request (Saving)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save() # This writes it to the hard drive
            return redirect('review_page') # This reloads the page to show new data
    else:
        form = ReviewForm()

    # 2. Fetch ALL records from the database
    # This is what makes them "permanent" on the page
    all_reviews = Review.objects.all().order_by('-created_at')

    # 3. Pass that list to the HTML
    return render(request, 'reviews.html', {
        'reviews': all_reviews, 
        'form': form
    })
   




from django.http import HttpResponse
from django.template.loader import render_to_string

def robots_txt(request):
    content = render_to_string("robots.txt")
    return HttpResponse(content, content_type="text/plain")











