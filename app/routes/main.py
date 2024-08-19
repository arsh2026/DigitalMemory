# app/routes/dashboard.py

from flask import Blueprint, render_template, request, redirect, url_for, session

# Define the blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        role = request.form['role']
        session['role'] = role
        if role == 'patient':
            return redirect(url_for('main.patient_dashboard'))
        elif role == 'family':
            return redirect(url_for('main.family_dashboard'))
    return render_template('dashboard.html')

@main_bp.route('/patient_dashboard')
def patient_dashboard():
    # Fetch family members and their photos, then render the page
    return render_template('patient_dashboard.html')

@main_bp.route('/family_dashboard')
def family_dashboard():
    # Provide options for adding family members, leaving notes, etc.
    return render_template('family_dashboard.html')
