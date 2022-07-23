import priaid_api as api
import config
from flask import Flask


api = api.Priaid(config.USERNAME, config.PASSWORD,
                 config.priaid_authservice_url,
                 config.priaid_healthservice_url, config.language)


