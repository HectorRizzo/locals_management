import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db

#cargando certificado del proyecto firebase
firebase_sdk = credentials.Certificate('pruebaslp-19813-firebase-adminsdk-2l6b4-36850be328.json')

#referencia al database en tiempo real de firebase
firebase_admin.initialize_app(firebase_sdk,{'databaseURL':'https://pruebaslp-19813-default-rtdb.firebaseio.com/'})

'''users = db.reference('/users')
users.push({
    'nombre': 'david',
    'apellido': 'yanez',
    'clave': '123456',
    'correo': 'dfyanez@espol.edu.ec',
    'tipo': 'propietario',
})'''

'''local = db.reference('/local')
local.push(
    {'PastelesChino':{
        'nombre': 'PastelesChino',
        'apertura': '08:00',
        'cierre': '16:00',
        'direccion': 'ESPOL',
        'tipo': 'restaurante',
        'capacidad': 60,
        'propietario': 'hector',
        'contacto': ['0989816645','0993386084'],
        },
    'PastelesCelex':{
    'nombre': 'PastelesCelex',
    'apertura': '08:00',
    'cierre': '16:00',
    'direccion': 'ESPOL',
    'tipo': 'restaurante',
    'capacidad': 60,
    'propietario': 'hector',
    'contacto': ['0989816645','0993386084'],}
        
    }
)'''


def getLocal(local):
    ref = db.reference('local')
    datos = ref.child(local)
    dic = datos.get()
    print(dic)

def addLocal(dic):
    ref = db.reference('local')    
    ref.update(dic)
 

def deleteLocal(local):
    ref = db.reference('local')
    ref.child(local).set({})

#deleteLocal("PastelesAbuelo")
#exit()


def updateLocal(local,datos_local):
    deleteLocal(local)
    addLocal(local,datos_local)
    
###Formato de dicionario de locales
"""dic = {local:{
        'nombre': local,
        'apertura': '08:00',
        'cierre': '16:00',
        'direccion': 'ESPOL',
        'tipo': 'restaurante',
        'capacidad': 60,
        'propietario': 'hector',
        'contacto': ['0989816645','0993386084'],
        }} """



def getUsuario(user):
    ref = db.reference('users')
    datos = ref.child(user)
    dic = datos.get()
    print(dic)


def addUsuario(dic):
    ref = db.reference('users')    
    ref.update(dic)
 

def deleteUser(user):
    ref = db.reference('user')
    ref.child(user).set({})

#deleteLocal("PastelesAbuelo")
#exit()


def updateUser(user,datos_user):
    deleteLocal(user)
    addLocal(user,datos_user)


getUsuario("-MhunkPtiLJBRUWpktK0")