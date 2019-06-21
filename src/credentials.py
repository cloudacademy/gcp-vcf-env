import json
from google.oauth2.service_account import Credentials


class credential_helper:
    @staticmethod
    def get_credentials(config):
        service_account_info = json.loads(
            config['credentials']['credential_key'])
        credentials = Credentials.from_service_account_info(
            service_account_info)
        credentials = credentials.with_scopes(
            ['https://www.googleapis.com/auth/cloud-platform'])
        credentials = credentials.with_subject(
            config['credentials']['credential_id'])
        return credentials
