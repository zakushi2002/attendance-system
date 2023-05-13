# GROUP 3 [20110002, 20110405, 20110420] [Nguyen Xuan Loc, Ha Tan Tho, Nguyen Huynh Thanh Toan]
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

credential = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(credential, {
    'databaseURL': "https://face-recordnition-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

databaseRef = db.reference('Students')
with open('./Data/data.json', 'r') as f:
    data = json.load(f)
# print(data)
# Insert data - Student to Firebase Realtime Database
for key, value in data.items():
    databaseRef.child(key).set(value)