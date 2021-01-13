import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = '(input)credential file.jason'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = '(input)spreadsheet url'
# 스프레스시트 문서 가져오기
doc = gc.open_by_url(spreadsheet_url)
# 시트 선택하기
worksheet = doc.worksheet('Sheet1')

cell_data = worksheet.acell('B1').value #특정 셀 데이터 가져오기
print(cell_data)

row_data = worksheet.row_values(1) #행데이터 가져오기
column_data = worksheet.col_values(1) #열 데이터 가져오기
# 범위(셀 위치 리스트) 가져오기
range_list = worksheet.range('A1:D2')
print(range_list)
# 범위에서 각 셀 값 가져오기
for cell in range_list:
    print(cell.value)

worksheet.update_acell('B1', 'b1 updated') #특정셀에 값 쓰기
worksheet.append_row(['new1', 'new2', 'new3', 'new4']) #행으로 데이터 추가하기
worksheet.insert_row(['new1', 'new2', 'new3', 'new4'], 4)
worksheet.resize(10,4) #시트크기 조절하기
gs = gc.create('새로운 테스트') #스프레드시트 생성하기
worksheet = gs.add_worksheet(title='시트1', rows='1', cols='1')
gs.share('(input)e-mail', perm_type='user', role='owner') #스프레드시트 공유 소유권 부여하기