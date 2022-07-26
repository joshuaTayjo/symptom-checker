from flask import (Blueprint, flash, g, redirect, render_template, request,
                   url_for)
from werkzeug.exceptions import abort
from .auth import login_required
from .db import get_db

bp = Blueprint('symptom_checker', __name__)


@bp.route('/')
def index():
    return render_template('symptom_checker/index.html')
