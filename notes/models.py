from django.db import models

# Create your models here.

# some methods for objects of the model
# Notes.objects.create
# Notes.objects.all()
# Notes.objects.get(pk='#')
# Notes.objects.filter(title_startswith='first')
# Notes.objects.filter(text__icontains='django')
# Notes.objects.exclude(text__icontains='django')
class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    # auto_now_add --> everytime a note is created
    # created field is populated with time that note
    # is created
    created = models.DateTimeField(auto_now_add=True)


