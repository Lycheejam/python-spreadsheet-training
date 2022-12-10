from google.oauth2 import service_account
import os


class ManipulationSpreadsheet:
    def main(self):
        credentials = self.authorize_credentials()
        print(credentials)

    def authorize_credentials(self, service_account_file_path=None):
        if service_account_file_path is None:
            # NOTICE: SENSITIVE INFO FILE !!!!!
            service_account_file_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "../secrets.json"
            )

        scopes = [
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/spreadsheets",
        ]
        credentials = service_account.Credentials.from_service_account_file(
            filename=service_account_file_path, scopes=scopes
        )

        return credentials


if __name__ == "__main__":
    get_data_to_spreadsheet = ManipulationSpreadsheet()
    get_data_to_spreadsheet.main()
