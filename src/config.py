import os

CONFIG = {
    'credentials': {
        'credential_id' : os.environ.get('CREDENTIAL_ID'),
        'credential_key': os.environ.get('CREDENTIAL_KEY'),
    },
    'environment_params': {
        'project_id' : os.environ.get('PROJECT_ID')
    }
}