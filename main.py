import datetime
from abc import ABCMeta
from pathlib import Path

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class WorksheetPreparer:
    def prepare(self, sheet_operator):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        p = Path(__file__)
        q = p.parent / 'gspread.json'

        credentials = ServiceAccountCredentials.from_json_keyfile_name(q, scope)
        gc = gspread.authorize(credentials)

        return gc.open('gspreadサンプル').worksheet(title=sheet_operator.TITLE)


class SheetOperator(metaclass=ABCMeta):
    TITLE = ''

    def __init__(self, worksheet_preparer: WorksheetPreparer):
        self.worksheet = worksheet_preparer.prepare(self)


class TimesSheetOperator(SheetOperator):
    TITLE = 'times'

    def record(self, running_time: int) -> None:
        current_datetime = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

        self.worksheet.append_row([current_datetime, running_time])


class UsersSheetOperator(SheetOperator):
    TITLE = 'users'

    def find(self):
        pass

if __name__ == '__main__':
    worksheet_preparer = WorksheetPreparer()
    TimesSheetOperator(worksheet_preparer).record(running_time=30)
