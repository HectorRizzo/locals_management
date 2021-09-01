import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask, jsonify, request
app = Flask(__name__)


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

@app.route('/getLocal/<string:local>')
def getLocal(local):
    ref = db.reference('local')
    datos = ref.child(local)
    dic = datos.get()
    return jsonify(dic)

@app.route('/addLocal',methods=['POST'])
def addLocal():
    ref = db.reference('local')    
    ref.update(request.json)
    
 

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




@app.route('/getUser/<string:user>')
def getUsuario(user):
    ref = db.reference('users')
    datos = ref.child(user)
    dic = datos.get()
    return dic

@app.route('/addUsuario',methods=['POST'])
def addUsuario():
    ref = db.reference('users')    
    ref.update(request.json)
    return request.json
 

def deleteUser(user):
    ref = db.reference('user')
    ref.child(user).set({})
    return user
    

#deleteLocal("PastelesAbuelo")
#exit()


def updateUser(user,datos_user):
    deleteUser(user)
    newUser = {user:datos_user}
    return addUsuario(newUser)
    

if __name__ =='__main__':
    app.run(debug=True, port=4000)

