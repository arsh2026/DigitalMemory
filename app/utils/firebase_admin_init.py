import firebase_admin
from firebase_admin import credentials, auth

# Path to your service account key JSON file
cred = credentials.Certificate('path/to/serviceAccountKey.json')

# Initialize the Firebase app
firebase_admin.initialize_app(cred)

def create_user(email, password):
    user = auth.create_user(
        email=email,
        password=password
    )
    return user

def verify_user_token(id_token):
    # Verifies the ID token and returns the decoded token
    decoded_token = auth.verify_id_token(id_token)
    return decoded_token