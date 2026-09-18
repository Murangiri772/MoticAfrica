from django import forms
from .models import Team
from .models import TicketBooking

class TeamRegistrationForm(forms.ModelForm):

    class Meta:
        model = Team

        fields = [
            'team_name',
            'captain_name',
            'phone_number',
            'email',
            'county',
            'number_of_members',
            'team_description',
        ]

        widgets = {
            'team_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter team name',
            }),

            'captain_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter captain name',
            }),

            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 0712345678',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address',
            }),

            'county': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter county',
            }),

            'number_of_members': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of team members',
                'min': '1',
            }),

            'team_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us briefly about your team...',
                'rows': 4,
            }),
        }

class TicketBookingForm(forms.ModelForm):

    class Meta:
        model = TicketBooking

        fields = [
            'full_name',
            'phone_number',
            'email',
            'ticket_type',
            'number_of_tickets',
        ]

        widgets = {

            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your full name'
                }
            ),

            'phone_number': forms.TextInput(
                attrs={
                    'placeholder': '07XXXXXXXX'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter your email'
                }
            ),

            'ticket_type': forms.Select(),

            'number_of_tickets': forms.NumberInput(
                attrs={
                    'min': 1,
                    'max': 20,
                    'placeholder': 'Number of tickets'
                }
            ),
        }