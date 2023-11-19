import time

from config import CONFIG

## Beginning of VCF block

import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def handler(event, context):
    credentials = get_credentials(event)
    project_id = event['environment_params']['project_id']
    
    service = build('storage', 'v1', credentials=credentials, cache_discovery=False)
    result = service.buckets().list(project=project_id).execute()
    if 'items' not in result:
        return False

    buckets = [bucket['name'] for bucket in result['items']]
    function_service = build('cloudfunctions', 'v1', credentials=credentials)
    result = function_service.projects().locations().functions().list(parent=f'projects/{project_id}/locations/-').execute()
    if 'functions' not in result:
        return False
    
    for function in result['functions']:
        if ('eventTrigger' in function and
            function['eventTrigger']['service'] == 'storage.googleapis.com' and
            any(bucket in function['eventTrigger']['resource'] for bucket in buckets)):
            return True

    return False

def get_credentials(event):
    service_account_info = json.loads(event['credentials']['credential_key'])
    credentials = Credentials.from_service_account_info(service_account_info)
    credentials = credentials.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])
    credentials = credentials.with_subject(event['credentials']['credential_id'])
    return credentials

## End of VCF block

def timed_handler(event, context):
    start = time.time()

    result = handler(event, context)

    end = time.time()
    print(end - start)

    return result

if __name__ == "__main__":
    result = timed_handler(CONFIG, None)
    print(result)