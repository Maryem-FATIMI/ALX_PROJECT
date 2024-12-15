from django.db import migrations
from django.db.models import Count

def handle_duplicate_emails(apps, schema_editor):
    CustomUser = apps.get_model('users', 'CustomUser')
    duplicate_emails = CustomUser.objects.values('email').annotate(
        email_count=Count('email')).filter(email_count__gt=1)
    
    for duplicate in duplicate_emails:
        users_with_duplicate_email = CustomUser.objects.filter(email=duplicate['email']).order_by('id')
        for index, user in enumerate(users_with_duplicate_email[1:], start=1):
            user.email = f"{user.email}_{index}"
            user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(handle_duplicate_emails),
    ]