from django.db import models
from datetime import datetime

# Create your models here.

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    event_date = models.DateTimeField(null=True, default=None)
    registration_deadline = models.DateTimeField(null=True, default=None)
    pictures = models.FileField(blank=True)
    # status = models.ForeignKey(Status, null=True, on_delete=models.CASCADE)
    # Note, I used this link but am not using a view at this point https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

class Image(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField( auto_now_add=True)

    class Meta:
        ordering=['-date']

    def __str__(self):
        return str(self.date)


# class Event(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=1000)
#     event_date = models.DateTimeField(null=True, default=None)
#     registration_deadline = models.DateTimeField(null=True, default=None)
#     # I got this from https://www.askpython.com/django/upload-files-to-django
#     flyer = models.FileField(upload_to='static/assets/', null=True)
#     # flyer = models.FilePathField(path=f'C:{os.sep}AlbuGierke Environmental Solutions{os.sep}Active Projects{os.sep}milescitywalleyes.com{os.sep}Django{os.sep}basePages{os.sep}static{os.sep}assets{os.sep}', null=True)
#     status = models.ForeignKey(Status, null=True, on_delete=models.CASCADE)
#     # Note, I used this link but am not using a view at this point https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(default=datetime.now())

#     def __str__(self):
#         return self.name

# class PostImage(models.Model):
#     post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
#     images = models.FileField(upload_to = 'images/')
 
#     def __str__(self):
#         return self.post.title        