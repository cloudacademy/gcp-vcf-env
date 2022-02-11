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

1. In `init.sh` (Mac/Linux)/`init.ps1` (Windows) replace YOUR_BITBUCKET_USER with the name of your Cloud Academy BitBucket user

1. Run `init.sh` (Mac/Linux)/`init.ps1` (Windows) to set up the environment

    - Enter your Cloud Academy BitBucket password/[app password](https://confluence.atlassian.com/bitbucket/app-passwords-828781300.html) when prompted.

1. Add the following line to `.gitignore` to avoid committing any sensitive information:

    ```
    .vscode/
    ```

1. Develop and debug functions using the `Current File (Integrated Terminal)` configuration (press F5 with the file open)

    If you see any errors with importing modules, ensure VS Code is configured to use the venv Python by checking the lower-left status bar in VS Code:

    ![venv Python in VS Code status bar](https://user-images.githubusercontent.com/3911650/153683320-b656c3c0-b268-4927-a186-81a301517d49.png)

## Update Dependencies

1. Run `init.sh` (Mac/Linux)/`init.ps1` (Windows) to set up the virtual environment again. (only the `venv/` directory is impacted by this operation)

## References

- [Google APIs Explorer](https://developers.google.com/apis-explorer)
- [OAuth2 Scopes for Google](https://developers.google.com/identity/protocols/googlescopes)
- [GCP Python Docs Samples](https://github.com/GoogleCloudPlatform/python-docs-samples)
