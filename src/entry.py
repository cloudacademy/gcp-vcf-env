from dotenv import load_dotenv
load_dotenv() 

import time
from config import CONFIG
import vcf

import os, sys
import google.auth

class credential_helper:
    credentials = None
    project_id = None

    @staticmethod
    def get_credentials(event):
        if not credential_helper.credentials:
            credential_helper.credentials, credential_helper.project_id = google.auth.default()
            if not credential_helper.project_id:
                credential_helper.project_id = credential_helper.credentials.quota_project_id
        return credential_helper.credentials

vcf.get_credentials = credential_helper.get_credentials

def timed_handler(event, context):
    start = time.time()
    result = vcf.handler(event, context)
    end = time.time()
    print(end - start)
    return result

def entry():
    if os.environ.get('CREDENTIAL_KEY'):
        # write credentials to file
        with open('/tmp/credentials.json', 'w', encoding="utf-8") as f:
            f.write(os.environ.get('CREDENTIAL_KEY'))
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/tmp/credentials.json'
    # cache credentials and handle project precedence (.config.env > gcloud default)
    credential_helper.get_credentials(None)
    if not os.environ.get('PROJECT_ID'):
        print('PROJECT_ID not set, attempting to use gcloud default project')
        if credential_helper.project_id:
            print(f'Using {credential_helper.project_id} as PROJECT_ID')
            CONFIG['environment_params']['project_id'] = credential_helper.project_id
        else:
            print('Could not find default project. Attempting to continue...', file=sys.stderr)

    result = timed_handler(CONFIG, None)
    print(result)

if __name__ == "__main__":
    entry()
