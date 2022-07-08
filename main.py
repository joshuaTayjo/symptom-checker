import requests
import config
import api_connection as api

auth_token = api.authenticate(config.USERNAME, config.PASSWORD,
                                config.priaid_authservice_url)

symptoms = requests.get(
    f'{config.priaid_healthservice_url}/symptoms?token={auth_token}&language={config.language}').json()
print(symptoms)
