import gspread
from gspread import Client, Spreadsheet, Worksheet
import os
import traceback
from pathlib import Path


class ManipulationSpreadsheet:
    def __init__(self) -> None:
        self.client = self.authorize_service_account()

    def main(self) -> None:
        spreadsheet = self.create_spreadsheet("test desu")
        self.share_spreadsheet(spreadsheet)

        data = [
            ["id", "name"],
            [1, "yamada"],
            [2, "suzuki"],
            [3, "tanaka"],
        ]

        response = self.data_update(spreadsheet, data)
        print(response)

        worksheet = self.get_sheet(spreadsheet)
        print(worksheet)

    def authorize_service_account(self, service_account_file_path: str = "") -> Client:
        if service_account_file_path == "":
            # NOTICE: SENSITIVE INFO FILE !!!!!
            service_account_file_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "../secrets.json"
            )

        try:
            return gspread.service_account(filename=Path(service_account_file_path))

        except Exception:
            print(traceback.format_exc())

    def create_spreadsheet(
        self, spreadsheet_name: str = "default spreadsheet name"
    ) -> Spreadsheet:
        try:
            return self.client.create(spreadsheet_name)
        except Exception:
            print(traceback.format_exc())

    def get_spreadsheet(self, spreadsheet_id: str) -> Spreadsheet:
        try:
            return self.client.open_by_key(spreadsheet_id)
        except Exception:
            print(traceback.format_exc())

    def get_sheet(self, spreadsheet: Spreadsheet, index: int = 0) -> Worksheet:
        try:
            return spreadsheet.get_worksheet(index)
        except Exception:
            print(traceback.format_exc())

    def share_spreadsheet(self, spreadsheet: Spreadsheet):
        # NOTE: replace mail address
        response = spreadsheet.share(
            "example@example.com", perm_type="user", role="writer"
        )

        return response

    def data_update(self, spreadsheet: Spreadsheet, data):
        response = spreadsheet.values_update(
            "Sheet1!A1",
            params={
                "valueInputOption": "RAW",
            },
            body={"values": data},
        )

        return response


if __name__ == "__main__":
    manipulation_spreadsheet = ManipulationSpreadsheet()
    manipulation_spreadsheet.main()
