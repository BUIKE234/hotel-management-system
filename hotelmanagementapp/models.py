from django.db import models

class RoomType(models.Model):
    ROOM_CHOICES = [
        ('deluxe', 'Deluxe Room'),
        ('executive', 'Executive Suite'),
        ('presidential', 'Presidential Suite'),
        ('single', 'Single Room'),
        ('double', 'Double Room'),
    ]
    name = models.CharField(max_length=20, choices=ROOM_CHOICES, unique=True)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    description = models.TextField(blank=True, null=True)
    capacity = models.PositiveBigIntegerField(default=2)
    

    def __str__(self):
        return self.get_name_display()

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    booked_at = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, default='pending')

    def save(self, *args, **kwargs):
        if self.check_in_date and self.check_out_date and self.room_type:
            days = (self.check_out_date - self.check_in_date).days
            if days > 0:
                self.total_price = days * self.room_type.price_per_night
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} - {self.room_type} - {self.check_in_date}"
