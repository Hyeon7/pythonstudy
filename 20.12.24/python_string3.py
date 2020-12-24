#41 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
#   ticker = "btc_krw"
ticker = "btc_krw"
a = ticker.upper()
print(a)
#42 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
#   ticker = "BTC_KRW"
ticker = "BTC_KRW"
a = ticker.lower()
print(a)
#43 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
word = "hello"
a = word.capitalize()
print(a)
#44 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
#   file_name = "보고서.xlsx"
file_name = "보고서.xlsx"
a = file_name.endswith("xlsx")
print(a)
#45 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
#   file_name = "보고서.xlsx"
file_name = "보고서.xlsx"
a = file_name.endswith(("xlsx", "xls"))
print(a)
#46 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
#   file_name = "2020_보고서.xlsx"
file_name = "2020_보고서.xlsx"
a = file_name.startswith("2020")
print(a)
#47 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
#   a = "hello world"
a = "hello world"
b = a.split(" ")
print(b)
#48 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
#   ticker = "btc_krw"
ticker = "btc_krw"
a = ticker.split("_")
print(a)
#49 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
#   date = "2020-05-01"
date = "2020-05-01"
a = date.split("-")
print(a)
#50 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
#   data = "039490     "
data = "039490     "
a = data.rstrip()
print(a)