from django.contrib.auth.models import User
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CrewConnect.settings')
django.setup()

if not User.objects.filter(username='akhila').exists():
    User.objects.create_superuser('akhila', 'akhilapolavarapu@gmail.com', 'Akhila123')
    print("Superuser created")
else:
    u = User.objects.get(username='akhila')
    u.set_password('Akhila123')
    u.save()
    print("Password reset")
