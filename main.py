import datetime
from pathlib import Path

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Spreadsheet:
    def prepare_worksheet(self):
        """worksheetを準備する。"""
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        p = Path(__file__)
        q = p.parent / 'gspread.json'

        credentials = ServiceAccountCredentials.from_json_keyfile_name(q, scope)
        gc = gspread.authorize(credentials)

        return gc.open('gspreadサンプル').sheet1

    def main(self, running_time):
        """準備されたworksheetに、現在の日時とrunning_timeを記録する"""
        worksheet = self.prepare_worksheet()

        current_datetime = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        worksheet.append_row([current_datetime, running_time])


if __name__ == '__main__':
    Spreadsheet().main(running_time=20)
