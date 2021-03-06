from django.core.management.base import BaseCommand
from rooms.models import Amenity

class Command(BaseCommand):

    help = 'This command creates amenities'
    
    def handle(self, *args, **options):


        amenities = [
            'Air conditioning',
            'Alarm Clock',
            'Balcony',
            'Bathroom',
            'Bathtub',
            'Bed Linen',
            'Boating',
            'Cable TV',
            'Carbon monoxide detectors',
            'Chairs',
            'Shower',
            'Stereo',
            'Swimming pool',
            'Toilet',
            'Towels',
            'TV',
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS('Amenities created!'))  
