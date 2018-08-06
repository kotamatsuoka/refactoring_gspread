import datetime
from pathlib import Path

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Spreadsheet:
    """worksheetへ記録する操作に加え、削除する操作をするクラスにする場合を考えてみる。"""

    def __init__(self):
        self.worksheet = self.prepare_worksheet()

    def prepare_worksheet(self):
        """worksheetを準備する。"""
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        p = Path(__file__)
        q = p.parent / 'gspread.json'

        credentials = ServiceAccountCredentials.from_json_keyfile_name(q, scope)
        gc = gspread.authorize(credentials)

        return gc.open('gspreadサンプル').sheet1

    def record(self, running_time):
        """準備されたworksheetに、現在の日時とrunning_timeを記録する"""
        # worksheet = self.prepare_worksheet() <-  __init__() へ引き上げ
        current_datetime = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

        self.worksheet.append_row([current_datetime, running_time])

    def delete(self):
        # worksheet = self.prepare_worksheet() <-  __init__() へ引き上げ

        # 具体的な記録を削除する処理は省略する
        self.worksheet.hoge()

if __name__ == '__main__':
    Spreadsheet().record(running_time=20)
