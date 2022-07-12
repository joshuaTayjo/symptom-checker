import config
import api_utils as api
import pandas as pd
import sqlalchemy as db
from sqlalchemy import text

auth_token = api.get_auth_token(config.USERNAME, config.PASSWORD,
                                config.priaid_authservice_url)

symptoms = api.get_all_symptoms(config.priaid_healthservice_url, auth_token,
                                config.language)
symptoms_df = pd.DataFrame(symptoms, columns=['ID', 'Name'])
symptoms_df.rename(columns={'ID': 'id', 'Name': 'symptom_name'},
                   inplace=True)
print(symptoms)
print(symptoms_df)
engine = db.create_engine('sqlite+pysqlite:///symptoms.db', future=True,
                          echo=True)
symptoms_df.to_sql('symptoms', engine, if_exists='replace', index=False)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM symptoms;"))
    print(result.all())
