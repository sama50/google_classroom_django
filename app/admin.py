from django.contrib import admin
from app.models import Classroom , JoinByClassroom , FilebyClassRoom , CommentByClassRoom
# Register your models here.

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('id','title','createdby','desc','classcode')

@admin.register(JoinByClassroom)
class JoinByClassroomAdmin(admin.ModelAdmin):
    list_display = ('id','classroom','user')

@admin.register(FilebyClassRoom)
class FilebyClassRoomAdmin(admin.ModelAdmin):
    list_display =('id','classroom','user','file')

@admin.register(CommentByClassRoom)
class CommentByClassRoomAdmin(admin.ModelAdmin):
    list_display = ('id','classroom','user','text')


    


