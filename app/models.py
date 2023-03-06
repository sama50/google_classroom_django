from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Classroom(models.Model):
    createdby = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    classcode = models.CharField(max_length=256)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class JoinByClassroom(models.Model):
    classroom = models.ForeignKey(to=Classroom, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.classroom.title
    
class FilebyClassRoom(models.Model):
    classroom = models.ForeignKey(to=Classroom, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media')

class CommentByClassRoom(models.Model):
    classroom = models.ForeignKey(to=Classroom, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField()


 
