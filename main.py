import datetime
from pathlib import Path

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class WorksheetPreparer:
    """worksheetを取り扱うクラス"""

    def prepare(self, sheet_title):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        p = Path(__file__)
        q = p.parent / 'gspread-sample.json'

        credentials = ServiceAccountCredentials.from_json_keyfile_name(q, scope)
        gc = gspread.authorize(credentials)

        return gc.open('gspreadサンプル').worksheet(title=sheet_title)


class TimesSheetOperator:
    """時間の記録を担当するクラス"""
    TITLE = "times"

    def __init__(self):
        self.worksheet = WorksheetPreparer().prepare(self.TITLE)

    def record(self, study_time):
        current_datetime = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        self.worksheet.append_row([current_datetime, study_time])


class UsersSheetOperator:
    """ユーザーの操作を担当するクラス"""
    TITLE = "users"

    def __init__(self):
        self.worksheet = WorksheetPreparer().prepare(self.TITLE)

    def find(self):
        pass

if __name__ == '__main__':
    TimesSheetOperator().record(study_time=20)
