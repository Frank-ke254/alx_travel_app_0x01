from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {"title": "Villa lodge", "description": "Nice beach house.", "location": "Mombasa", "price_per_night": 120.00},
            {"title": "The Ark", "description": "Modern apartment in Kiambu.", "location": "Kiambu", "price_per_night": 80.00},
            {"title": "Nairobi Lodge", "description": "Experience wildlife in style", "location": " Nairobi", "price_per_night": 200.00},
        ]

        for listing_data in sample_listings:
            Listing.objects.get_or_create(**listing_data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded sample listings!"))
