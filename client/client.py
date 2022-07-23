from flask import Blueprint, render_template

client_bp=Blueprint('client_bp',__name__, template_folder='templates',static_folder='static',static_url_path='/client/static')

@client_bp.route('/')
def index():
    return render_template('index.html')

