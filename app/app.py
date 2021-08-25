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

'''#obtener datos
ref = db.reference('local')
datos = ref.child('-Mhv0-VwxMdobUmhQ4Ml')

#Load JSON string into a dictionary
dic = datos.get()
#Loop along dictionary keys
for i in dic:
    print(i,dic[i])'''

#metodo consulta de datos de un local
def obtenerDatosLocal(local):
    ref = db.reference('local')
    datos = ref.child('-Mhv0-VwxMdobUmhQ4Ml')

    #Load JSON string into a dictionary
    dic = datos.get()
    #Loop along dictionary keys
    print("Detalles del local",local,":")
    for key,value in dic[local].items():
        print('\t',key,':',value)

obtenerDatosLocal('PastelesChino')