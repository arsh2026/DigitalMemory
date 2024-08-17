import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1r3shrwfafy23@sv01s'
    FIREBASE_ADMIN_CREDENTIALS = r'C:\Users\Hp\Downloads\digitalmemory-fbe68-firebase-adminsdk-do0ze-81310fe494.json'