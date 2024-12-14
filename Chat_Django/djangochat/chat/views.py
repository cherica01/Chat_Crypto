from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from cryptography.fernet import Fernet
from cryptography.fernet import Fernet
from django.http import HttpResponse

from django.http import HttpResponse
from cryptography.fernet import Fernet
from .models import Message



def encrypt_message(key, message):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode()).decode()


def decrypt_message(key, encrypted_message):
    try:
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_message.encode()).decode()
    except Exception:
        return "Message chiffré. Clé invalide."

# Vues
def room(request , room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    rooms = Room.objects.all() 
    return render(request , 'room.html' , {
        'username' : username ,
        'room' : room ,
        'room_details' : room_details ,
        'rooms': rooms,
    })
def home(request):
    return render(request, 'home.html')
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name = room).exists():
        return redirect('/'+ room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name = room)
        new_room.save()
        return redirect('/'+ room + '/?username=' + username)
from cryptography.fernet import Fernet
from django.http import HttpResponse

from django.http import HttpResponse
from cryptography.fernet import Fernet
from .models import Message

def send(request):
    # Récupération des paramètres
    message = request.POST.get('message')
    username = request.POST.get('username')
    room_id = request.POST.get('room_id')
    encryption_key = request.POST.get('encryption_key')

    
    if not message or not username or not room_id:
        return HttpResponse('Tous les champs (message, utilisateur, salle) sont requis.', status=400)

  
    if encryption_key:
        try:
            fernet = Fernet(encryption_key)
            encrypted_message = fernet.encrypt(message.encode()).decode()
            new_message = Message.objects.create(
                value=encrypted_message, user=username, room=room_id, is_encrypted=True
            )
        except ValueError:
            return HttpResponse('Clé de chiffrement invalide.', status=400)
    else:
        
        new_message = Message.objects.create(
            value=message, user=username, room=room_id, is_encrypted=False
        )

    new_message.save()
    return HttpResponse('Message envoyé avec succès')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id).order_by('date')
    encryption_key = request.GET.get('decryption_key')  # La clé de déchiffrement envoyée par le client
    message_list = []

    for msg in messages:
        if msg.is_encrypted and encryption_key:
            decrypted_value = decrypt_message(encryption_key, msg.value)
        else:
            decrypted_value = msg.value if not msg.is_encrypted else "Message chiffré."
        message_list.append({
            "user": msg.user,
            "value": decrypted_value,
            "date": msg.date
        })

    return JsonResponse({"messages": message_list})
