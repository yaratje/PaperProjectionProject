import firebase_admin
from firebase_admin import credentials, db


def databse_setup():
    # Initialize app
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://allert-app-3fa43-default-rtdb.europe-west1.firebasedatabase.app/' 
    })

    
def trigger_alert(user):
    # Reference to the alert flag
    #user123
    who = 'alerts/' + user
    ref = db.reference(who)
    # Trigger the alert
    ref.set(True)
    print("✅ Alert sent to watch.")
