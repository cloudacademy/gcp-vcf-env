# gcp-vcf-env

Envrionment for working with GCP VCFs

## Getting started

1. Ensure Python 3.6+ is installed on your system

1. Create a GCP project

1. Create a service account for running the VCFs

1. Create a JSON key for the service account

1. Add the service account to the project _Owner_ or _Viewer_ role

1. In `.vscode/launch.json` fill in the `CREDENTIAL_KEY`, `CREDENTIAL_ID` and `PROJECT_ID` for the service account. Be sure to escape the JSON. Avoid using online tools to do this due to the sensitive nature of what you are escaping. The resulting `env` map will resemble:
    ```json
    {
        "CREDENTIAL_ID"  : "your-service-account@your-project.iam.gserviceaccount.com",
        "CREDENTIAL_KEY": "{\"type\":\"service_account\",\"project_id\":\"your-project\",\"private_key_id\":\"...}",
        "PROJECT_ID"     : "your-project"
    }
    ```

1. Run `init.ps1` (Windows)/`init.sh` (Mac/Linux) to set up the environment

1. Add the following line to `.gitignore` to avoid committing any sensitive information:

    ```
    .vscode/
    ```

1. Develop and debug functions using the `Current File (Integrated Terminal)` configuration (press F5 with the file open)

## References

- [Google APIs Explorer](https://developers.google.com/apis-explorer)
- [OAuth2 Scopes for Google](https://developers.google.com/identity/protocols/googlescopes)