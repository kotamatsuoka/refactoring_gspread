import datetime
from pathlib import Path

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def main(running_time):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    p = Path(__file__)
    q = p.parent / 'gspread.json'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(q, scope)
    gc = gspread.authorize(credentials)
    worksheet = gc.open('gspreadサンプル').sheet1

    current_datetime = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    worksheet.append_row([current_datetime, running_time])


if __name__ == '__main__':
    main(running_time=20)
