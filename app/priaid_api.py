import hmac
import requests
import base64
import json


class Priaid:
    def __init__(self, username, password, auth_url, health_url, language):
        """
        :param username: app username
        :param password: app password
        :param auth_url: priaid login url (https://authservice.priaid.ch/login)
        :param health_url: priaid health service url (https://healthservice.priaid.ch)
        :param language: language code (en-gb, de-ch, fr-fr, es-es)
        """
        self._health_url = health_url
        self._language = language
        self._auth_token = self.get_auth_token(username, password, auth_url)

    def get_auth_token(self, username: str, password: str, auth_url: str):
        """
        Connect to the API and get the auth token
        :param username: username for app
        :param password: password for app
        :param auth_url: url to connect to oauth app service
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
            print('Error occurred when authenticating: \n', e)
            return None

    def _load_from_api(self, action: str):
        extra_params = f'token={self._auth_token}&language={self._language}'
        if '?' not in action:
            action += f'?{extra_params}'
        else:
            action += f'&{extra_params}'

        response = requests.get(f'{self._health_url}/{action}')

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print('Error occurred when connecting to API: \n', e)
            return None

        return response.json()

    def get_all_symptoms(self):
        """
        Get all symptoms from the API
        :return: list - all symptoms from the json returned by app
        """
        return self._load_from_api('symptoms')

    def get_all_issues(self):
        """
        Get all issues from the API
        :return: list - all issues from the json returned by app
        """
        return self._load_from_api('issues')

    def get_issue(self, issue_id):
        """
        Get issue from the API
        :param issue_id: issue id
        :return: dict - issue from the json returned by app
        """
        return self._load_from_api(f'issues/{issue_id}/info')

    def get_diagnosis(self, symptoms: list, gender: str,
                      year_of_birth):
        """
        :param symptoms: list of ints of selected symptom ids
        :param gender: string 'male' or 'female'
        :param year_of_birth: 4-digit int
        :return: dict of possible diagnoses
        """
        serialized_symptoms = json.dumps(symptoms)
        action = f'diagnosis?symptoms={serialized_symptoms}' \
                 f'&gender={gender}' \
                 f'&year_of_birth={year_of_birth}'
        return self._load_from_api(action)

    def get_all_body_locations(self):
        """
        :return: list of body locations from app json data
        """
        return self._load_from_api('body/locations')

    def get_body_sublocations(self, body_location_id):
        """
        :param body_location_id: body location id
        :return: list of body sublocations from app json data based on
        body location id
        """
        return self._load_from_api(
            f'body/locations/{body_location_id}')

    def get_sublocation_symptoms(self, body_sublocation_id,
                                 age_gender_selector: str):
        """
        :param body_sublocation_id: body sublocation id
        :param age_gender_selector: 'man' 'woman' 'boy' or 'girl', age cutoff
        is 12 and above for adults
        :return: list of symptoms from app json data based on body sublocation
        id
        """
        return self._load_from_api(
            f'symptoms/{body_sublocation_id}/{age_gender_selector}')

    def get_related_symptoms(self, symptoms: list, gender: str,
                             year_of_birth):
        """
        :param symptoms: list of symptom id's
        :param gender: str 'male' or 'female'
        :param year_of_birth: str or int of birth year
        :return: list of symptoms which may be related to the symptoms in
        symptoms list to refine diagnoses
        """
        serialized_symptoms = json.dumps(symptoms)
        action = f'symptoms/proposed?symptoms={serialized_symptoms}' \
                 f'&gender={gender}' \
                 f'&year_of_birth={year_of_birth}'
        return self._load_from_api(action)
