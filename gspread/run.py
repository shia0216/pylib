import gspread
import pandas
import gspread_dataframe


class GoogleCloud():
    def __init__(self, path: str, key: str) -> None:
        self.spreadsheet = gspread.service_account(filename=path).open_by_key(key)

    def read_sheet(self, sheetname: str) -> pandas.DataFrame:
        sheet = self.spreadsheet.worksheet(sheetname)
        return pandas.DataFrame(sheet.get_all_values())

    def write_sheet(self, sheetname: str, df: pandas.DataFrame, rows: int=10, cols: int=5) -> None:
        sheet = self.spreadsheet.add_worksheet(sheetname, rows=100, cols=26)
        gspread_dataframe.set_with_dataframe(sheet, df)
        return


if __name__ == '__main__':
    # Google Cloud service account json path
    path_authentication = ''

    # Spreadsheet access key
    key_spreadsheet = ''

    # sample: copy data from sheet1 to sheet2
    spreadsheet = GoogleCloud(path_authentication, key_spreadsheet)
    df = spreadsheet.read_sheet('sheet1')
    spreadsheet.write_sheet('sheet2', df)
