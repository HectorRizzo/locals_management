import firebase_admin
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
    {
        'nombre': 'PastelesChino',
        'apertura': '08:00',
        'cierre': '16:00',
        'direccion': 'ESPOL',
        'tipo': 'restaurante',
        'capacidad': 60,
        'propietario': 'hector',
        'contacto': ['0989816645','0993386084'],
    }
)'''

#obtener datos
ref = db.reference('users')
datos = ref.child('-MhuoF8tSDPhTYQedOAS')
print(datos.get())
