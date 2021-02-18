from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User

class Command(BaseCommand):

    help = 'This command creates many users'


    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default=2, type=int, help='How many users do you want to create'  # type=int -> number가 str인 문제를 해결
        )


    def handle(self, *args, **options):
        number = options.get('number', 1)
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {'is_staff': False, 'is_superuser': False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} users created!'))  


# console창에서 python manage.py seed_users를 그냥 실행해주면 2개 유저 생성 (default = 2)
# python manage.py seed_users --number 50 : 50개 유저 생성
