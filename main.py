import hmac
import requests
import base64
import config

raw_hash = hmac.new(bytes(config.PASSWORD, encoding='utf-8'),
                    config.priaid_authservice_url.encode('utf-8'),
                    digestmod='MD5').digest()
hash_str = base64.b64encode(raw_hash).decode()

bearer_credentials = f'{config.USERNAME}:{hash_str}'
post_headers = {'Authorization': f'Bearer {bearer_credentials}'}
auth_response = requests.post(config.priaid_authservice_url,
                              headers=post_headers)

auth_token = auth_response.json()['Token']

symptoms = requests.get(
    f'{config.priaid_healthservice_url}/symptoms?token={auth_token}&language={config.language}').json()
print(symptoms)
