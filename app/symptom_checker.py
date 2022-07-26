from flask import (Blueprint, flash, g, redirect, render_template, request,
                   url_for)
from werkzeug.exceptions import abort
from .auth import login_required
import app.config as config
from .priaid_api import Priaid

health_api = Priaid(config.USERNAME, config.PASSWORD,
                    config.priaid_authservice_url,
                    config.priaid_healthservice_url, config.language)

bp = Blueprint('symptom_checker', __name__)


@bp.route('/')
def index():
    return render_template('symptom_checker/index.html')


@bp.route('/check-symptoms', methods=('GET', 'POST'))
@login_required
def check_symptoms():
    body_locations = health_api.get_all_body_locations()
    all_symptoms = health_api.get_all_symptoms()
    return render_template('symptom_checker/check_symptoms.html',
                           body_locations=body_locations,
                           all_symptoms=all_symptoms)
