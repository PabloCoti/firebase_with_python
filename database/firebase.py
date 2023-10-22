import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('fir-w-python-c4463-firebase-adminsdk-xosvp-ad45bb5131.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': "https://fir-w-python-c4463-default-rtdb.firebaseio.com/"
})

ref = db.reference('/todo_list')
if not ref:
    ref.set({
        'todo_list': {}
    })
