import os

CONFIG = {
    'client_id'     : os.environ.get('CREDENTIAL_ID'),
    'client_secret' : os.environ.get('CREDENTIAL_KEY'),
    'project_id'    : os.environ.get('PROJECT_ID')
}

EVENT_CONFIG = {
    'credentials': {
        'credential_id' : CONFIG['client_id'],
        'credential_key': CONFIG['client_secret'],
    },
    'environment_params': {
        'project_id' : CONFIG['project_id']
    }
}