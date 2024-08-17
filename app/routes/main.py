from flask import Blueprint, render_template, flash, Response

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    print("heyooo")
    flash('Donee')
    return Response('')