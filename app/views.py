from django.shortcuts import render ,redirect
from app.models import Classroom , JoinByClassroom ,FilebyClassRoom , CommentByClassRoom
import uuid
# Create your views here.

def index(request):

    all_class_room_by_user  = Classroom.objects.filter(createdby=request.user)
    all_class_room_join_user = JoinByClassroom.objects.filter(user=request.user)

    return render(request,'index.html',{'all_class_room_by_user':all_class_room_by_user,'all_class_room_join_user':all_class_room_join_user})

def create_classroom(request):
    if request.method == 'POST':

        classroomname = request.POST.get('classroomname')
        desc = request.POST.get('desc')
        code = uuid.uuid4()
        data = Classroom(createdby=request.user,title=classroomname,desc=desc,classcode=code)
        data.save()
        JoinByClassroom(classroom=data,user=request.user).save()
        return redirect('index')
    
    return redirect('index')



def openclassroom(request,id):
    if Classroom.objects.filter(classcode=id).exists()==False:
        return redirect('/')
    get_class_room = Classroom.objects.get(classcode=id)
    all_user = JoinByClassroom.objects.filter(classroom=get_class_room)
    file_class = FilebyClassRoom.objects.filter(classroom=get_class_room)
    comment_class = CommentByClassRoom.objects.filter(classroom=get_class_room)
    print("==========")
    print(all_user)
    return render(request,'stream.html',{'get_class_room':get_class_room ,'file_class':file_class,'comment_class':comment_class,'all_user':all_user})

def addcomments(request):
    if request.method=='POST':
        idofroom = request.POST.get('idofclassroom')
        comment = request.POST.get('comment')
        currentpath = request.POST.get('currentpath')
        get_room = Classroom.objects.get(id=idofroom)

        CommentByClassRoom(classroom=get_room,user=request.user,text=comment).save()
        return redirect(currentpath)
    else:
        return redirect('index')

def addfile(request):
    if request.method=='POST':
        idofroom = request.POST.get('idofclassroom')
        file = request.FILES.get('sendfile')
        currentpath = request.POST.get('currentpath')
        get_room = Classroom.objects.get(id=idofroom)
        print(file)
        FilebyClassRoom(classroom=get_room,user=request.user,file=file).save()
        return redirect(currentpath)
    else:
        return redirect('index')

def joinclassroom(request):
    if request.method =='POST':
        roomid = request.POST.get('roomid')
        currenturl = request.POST.get('currenturl')
        print(roomid)
        print(currenturl)
        print("========")
        if Classroom.objects.filter(classcode=roomid).exists():
            print("===============")
            if JoinByClassroom.objects.filter(classroom=Classroom.objects.filter(classcode=roomid).first(),user=request.user).exists():
                return redirect('/')

            else:
                print("=====================")
                JoinByClassroom(classroom=Classroom.objects.filter(classcode=roomid).first(),user=request.user).save()
                return redirect(currenturl)
        else:
            return redirect('/')
    else:
        return redirect('/')