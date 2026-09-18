

from django.contrib import admin
from .models import Team, TicketBooking


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'team_name',
        'captain_name',
        'county',
        'number_of_members',
        'ticket_number',
        'payment_amount',
        'payment_status',
        'payment_reference',
        'created_at',
    )

    search_fields = (
        'team_name',
        'captain_name',
        'phone_number',
        'email',
        'county',
        'ticket_number',
        'payment_reference',
        'payment_status',
    )

    list_filter = (
        'county',
        'created_at',
    )

    ordering = (
        '-created_at',
    )

    readonly_fields = (
        'ticket_number',
        'created_at',
    )


@admin.register(TicketBooking)
class TicketBookingAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'ticket_type',
        'number_of_tickets',
        'payment_status',
        'phone_number',
        'booking_reference',
        'created_at',
    )
    list_filter = (
        'ticket_type',
        'payment_status',
        'created_at',
    )

    search_fields = (
        'full_name',
        'phone_number',
        'email',
        'booking_reference',
    )

    list_filter = (
        'ticket_type',
        'created_at',
    )

    ordering = (
        '-created_at',
    )

    readonly_fields = (
        'booking_reference',
        'created_at',
    )