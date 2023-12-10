import colorfield.fields
import django.db.models.deletion
from django.db import migrations, models
import Task.models as models

class Migration(migrations.Migration):
    dependencies = [('Task', '0001_initial')]
    
    def insertData(app, schema_editor):
        models.Category(name = 'Ninguna', description='').save()
    
    operations = [
        migrations.RunPython(insertData)
    ]