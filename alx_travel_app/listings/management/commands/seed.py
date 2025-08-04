import random
from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker

class Command(BaseCommand):
    help = 'Seeds the database with sample listings'

    def handle(self, *args, **options):
        self.stdout.write('Seeding the database...')
        fake = Faker()
        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=3),
                price=random.uniform(50.0, 500.0)
            )
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
