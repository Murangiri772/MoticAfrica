from django.shortcuts import render, redirect
from .models import Team, TicketBooking

from .forms import TeamRegistrationForm, TicketBookingForm
import qrcode
from io import BytesIO
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def starter(request):
    return render(request, 'starter-page.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')





def team_registration(request):

    if request.method == 'POST':
        form = TeamRegistrationForm(request.POST)

        if form.is_valid():
            team = form.save()

            return redirect(
                'team_success',
                team_id=team.id
            )

    else:
        form = TeamRegistrationForm()

    return render(request, 'team_registration.html', {
        'form': form
    })


def team_success(request, team_id):

    team = Team.objects.get(id=team_id)

    return render(request, 'team_success.html', {
        'team': team
    })


def team_ticket(request, team_id):

    team = Team.objects.get(id=team_id)

    return render(request, 'team_ticket.html', {
        'team': team
    })
def teams(request):
    all_teams = Team.objects.all().order_by('-created_at')

    return render(request, 'teams.html', {
        'teams': all_teams
    })
def battle(request):
    return render(request, 'battle.html')
def gallery(request):
    return render(request, 'gallery.html')
def tickets(request):
    return render(request, 'tickets.html')
def tickets(request):
    return render(request, 'tickets.html')

def ticket_booking(request):
    ticket_type = request.GET.get('type', 'Regular')

    prices = {
        'Regular': 500,
        'VIP': 1500,
        'VVIP': 3000,
    }

    if ticket_type not in prices:
        ticket_type = 'Regular'

    if request.method == 'POST':
        form = TicketBookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)

            booking.ticket_price = prices.get(
                booking.ticket_type,
                500
            )

            booking.save()

            return redirect(
                'ticket_success',
                booking_id=booking.id
            )
    else:
        form = TicketBookingForm(
            initial={
                'ticket_type': ticket_type
            }
        )

    return render(
        request,
        'ticket_booking.html',
        {
            'form': form,
            'ticket_type': ticket_type,
            'price': prices[ticket_type],
        }
    )


def ticket_success(request, booking_id):

    booking = TicketBooking.objects.get(id=booking_id)

    return render(request, 'ticket_success.html', {
        'booking': booking
    })
def ticket_qr(request, booking_id):

    booking = TicketBooking.objects.get(id=booking_id)

    verification_url = request.build_absolute_uri(
        f"/tickets/verify/{booking.booking_reference}/"
    )

    qr = qrcode.make(verification_url)

    buffer = BytesIO()
    qr.save(buffer, format='PNG')

    return HttpResponse(
        buffer.getvalue(),
        content_type='image/png'
    )
def verify_ticket(request, booking_reference):

    try:
        booking = TicketBooking.objects.get(
            booking_reference=booking_reference
        )

        if booking.payment_status == 'Paid':

            return render(request, 'verify_ticket.html', {
                'booking': booking,
                'valid': True,
                'status': 'Paid'
            })

        elif booking.payment_status == 'Used':

            return render(request, 'verify_ticket.html', {
                'booking': booking,
                'valid': False,
                'used': True
            })

        else:

            return render(request, 'verify_ticket.html', {
                'booking': booking,
                'valid': False,
                'pending': True
            })

    except TicketBooking.DoesNotExist:

        return render(request, 'verify_ticket.html', {
            'valid': False,
            'not_found': True
        })