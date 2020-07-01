from django.shortcuts import render

from .models import User, Room
from django.http import HttpResponse
import json

def inicio(request):
    return render(request,'index.html')


def return_users(request):

    users = User.objects.all()

    print(users[0])

    data = []

    for user in users:
        context ={
            'id': user.id,
            'name': user.name,
            'lastname': user.lastname,
            'email': user.email,
            'phone': user.phone,
            'anfitrion': user.anfitrion,
        }
        data.append(context)

    return HttpResponse(json.dumps(data))


def return_rooms(request):
    rooms = Room.objects.all()

    #print(rooms)

    data=[]

    for room in rooms:
        aux = {
            'id': room.id,  
            'created': str(room.created_date),
            'id_user': {
                'name': room.id_user.name,
                'last_name': room.id_user.lastname,
                'phone': room.id_user.phone,
                'email': room.id_user.email,
            },
            'picture': str(room.picture),
            'price': room.price,
            'nearest_places': room.nearest_places,
            'mts2': room.mts2,
            'furniture': room.furniture,
            'private_bath': room.private_bath,
            'wifi': room.wifi,
            'closet': room.closet,
            'kitchen': room.kitchen,
            'pet': room.pet,
            'washing_machine': room.washing_machine,
            'furnished': room.furnish,
            'tv': room.tv,
            'smoke': room.smoke,
            'couple': room.couple,
            'family_atmosphere': room.family_atmosphere,
            'description': room.description,
            'available': room.available,
        }
        
        data.append(aux)

    return HttpResponse(json.dumps(data))


def edit_user(request,id, anfi):
    
    user = User.objects.get(id = id)
    print(user)
    user.anfitrion = anfi
    user.save()
    print(user)
    
    data = {
        'name' : user.name,
        'lastname': user.lastname,
        'email': user.email,
        'anfitrion' : user.anfitrion,
    }

    return HttpResponse(json.dumps(data))

def signup(request,nombre,apellido,passwd,email,lugar,anfi,desc,tel):
    try:
        u = User(name=nombre,lastname=apellido,password=passwd,
                email=email,location=lugar,anfitrion=anfi,description=desc,phone=tel)
        u.save()
        print(u.id)
        data={
            'status':'ok',
            'nombre': nombre,
            'apellido': apellido,
            'email':email,
            'message': 'El usuario se creo correctamente'
        }
    except Exception as e:
        print(e)
        oa ={'status':'faile','message':'Email no valido', 'error':str(e)}
        return HttpResponse(json.dumps(oa))
    print(data)
    return HttpResponse(json.dumps(data))


def create_room(request, iu, price,ne_pl,mts2,furn,pri_bath,wifi,
                closet,kitchen,pet,w_m,furnished,tv,smoke,couple,family,desc):
    
    user = User.objects.get(id=iu)
    try:
        r = Room(id_user=user,price=price,nearest_places=ne_pl,mts2=mts2,
                furniture=furn,private_bath=pri_bath,wifi=wifi,closet=closet,
                kitchen=kitchen,pet=pet,washing_machine=w_m,furnish=furnished,
                tv=tv,smoke=smoke,couple=couple,family_atmosphere=family,description=desc)
        r.save()
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps(str(e)))

    return HttpResponse("Romm creado")

