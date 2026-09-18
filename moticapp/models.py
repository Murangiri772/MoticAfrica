from django.db import models
import uuid

class Team(models.Model):
    team_name = models.CharField(max_length=150)
    captain_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    county = models.CharField(max_length=100)
    number_of_members = models.PositiveIntegerField()
    team_description = models.TextField(blank=True)

    ticket_number = models.CharField(
        max_length=30,
        blank=True,
        default=""
    )
    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Cancelled', 'Cancelled'),
    ]
    payment_reference = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='Pending'
    )

    payment_reference = models.CharField(
        max_length=100,
        blank=True
    )

    payment_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=5000
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = f"MCB-{uuid.uuid4().hex[:8].upper()}"

        super().save(*args, **kwargs)

        class TicketBooking(models.Model):

            TICKET_TYPES = [
                ('Regular', 'Regular'),
                ('VIP', 'VIP'),
                ('VVIP', 'VVIP'),
            ]

            full_name = models.CharField(max_length=150)

            phone_number = models.CharField(max_length=20)

            email = models.EmailField()

            ticket_type = models.CharField(
                max_length=20,
                choices=TICKET_TYPES
            )

            number_of_tickets = models.PositiveIntegerField()

            booking_reference = models.CharField(
                max_length=30,
                unique=True,
                blank=True
            )

            created_at = models.DateTimeField(
                auto_now_add=True
            )

            def save(self, *args, **kwargs):
                if not self.booking_reference:
                    self.booking_reference = (
                        f"MT-{uuid.uuid4().hex[:8].upper()}"
                    )

                super().save(*args, **kwargs)

            def __str__(self):
                return f"{self.full_name} - {self.ticket_type}"

class TicketBooking(models.Model):

    TICKET_TYPES = [
        ('Regular', 'Regular'),
        ('VIP', 'VIP'),
        ('VVIP', 'VVIP'),
    ]

    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Used', 'Used'),
        ('Cancelled', 'Cancelled'),
    ]

    full_name = models.CharField(max_length=150)

    phone_number = models.CharField(max_length=20)

    email = models.EmailField()

    ticket_type = models.CharField(
        max_length=20,
        choices=TICKET_TYPES
    )

    number_of_tickets = models.PositiveIntegerField()

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='Pending'
    )
    ticket_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    booking_reference = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        if not self.booking_reference:
            self.booking_reference = (
                f"MT-{uuid.uuid4().hex[:8].upper()}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} - {self.ticket_type}"