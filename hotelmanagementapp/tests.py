from django.test import TestCase
from django.urls import reverse


class BookingSuccessViewTests(TestCase):
    def test_booking_success_returns_404_for_missing_booking(self):
        response = self.client.get(reverse('booking_success', args=[999999]))

        self.assertEqual(response.status_code, 404)
