import requests
import config
import api_utils as api

auth_token = api.get_auth_token(config.USERNAME, config.PASSWORD,
                                config.priaid_authservice_url)

symptoms = api.get_all_symptoms(config.priaid_healthservice_url, auth_token,
                                config.language)

print(symptoms)
