from google.oauth2 import service_account
import gspread
import os
import traceback


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

        try:
            credentials = service_account.Credentials.from_service_account_file(
                filename=service_account_file_path, scopes=scopes
            )

            return gspread.authorize(credentials)

        except Exception:
            print(traceback.format_exc())

    def create_spreadsheet(self, authorized_credential, spreadsheet_name):
        try:
            return authorized_credential.create(spreadsheet_name)
        except Exception:
            print(traceback.format_exc())

    def get_spreadsheet(self, authorized_credential, spreadsheet_id):
        try:
            return authorized_credential.open_by_key(spreadsheet_id)
        except Exception:
            print(traceback.format_exc())

    def get_sheet(self, spreadsheet):
        try:
            return spreadsheet.sheet1()
        except Exception:
            print(traceback.format_exc())

    def share_spreadsheet(self, spreadsheet):
        # NOTE: replace mail address
        response = spreadsheet.share(
            "example@example.com", perm_type="user", role="writer"
        )

        return response

    def value_update_spreadsheet(self, spreadsheet, formated_results):
        response = spreadsheet.values_update(
            "Sheet1!A1",
            params={
                "valueInputOption": "RAW",
            },
            body={"values": formated_results},
        )

        return response


if __name__ == "__main__":
    get_data_to_spreadsheet = ManipulationSpreadsheet()
    get_data_to_spreadsheet.main()
