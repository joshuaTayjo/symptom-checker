from flask import Blueprint

app_bp = Blueprint('app_bp', __name__)

@app_bp.route('/greeting')
def greeting():
    return {'greeting':'Hello from Flask!'}
