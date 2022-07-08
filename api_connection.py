import hmac
import requests
import config
import base64


def authenticate(username, password, auth_url):
    """
    Connect to the API and get the auth token
    :param username: username for api
    :param password: password for api
    :param auth_url: url to connect to oauth api service
    :return: str - auth token
    """
    try:
        raw_hash = hmac.new(bytes(password, encoding='utf-8'),
                            auth_url.encode('utf-8'),
                            digestmod='MD5').digest()
        hash_str = base64.b64encode(raw_hash).decode()

        bearer_credentials = f'{username}:{hash_str}'
        post_headers = {'Authorization': f'Bearer {bearer_credentials}'}
        auth_response = requests.post(auth_url,
                                      headers=post_headers)

        return auth_response.json()['Token']
    except Exception as e:
        print('Error occured when authenticating: \n', e)
        return None
