from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.utils.firebase_admin_init import create_user, verify_user_token  # Import Firebase functions

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            create_user(email, password)
            flash('Account created successfully', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login here using Firebase Client SDK
        flash('Logged in successfully', 'success')
        return redirect(url_for('main.index'))
    return render_template('login.html')

@auth_bp.route('/verify', methods=['POST'])
def verify():
    id_token = request.json.get('idToken')
    try:
        decoded_token = verify_user_token(id_token)
        return {'status': 'success', 'uid': decoded_token['uid']}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}, 401
