import datetime
import urllib.request
import random

# api 응답을 불러오는 get_request_url 함수선언
from pip._vendor import requests


def get_request_url(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


# 이용자가 버스번호를 입력

print(" ")
car = str(input('>> 저상버스 운행정보를 조회할 정류소의 ID를 입력해주세요 : '))

# 버스가 예약되었는지 아닌지 확인
reservation = random.randint(1,10)




# 엑셀시트 연계하기








# 공공데이터포털로부터 API 받아오기 설정

key = ''
busRouteld = car
queryParams = 'serviceKey='+key+'&stId='+busRouteld+'&'
url = 'http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId?'+queryParams

print('데이터 출처 : ' + url)


# xml 파일 파싱해서 json 형태로 변환

import xmltodict
import json

content = requests.get(url).content
dict = xmltodict.parse(content)
jsonString = json.dumps(dict['ServiceResult']['msgBody'], ensure_ascii = False)
json0bj = json.loads(jsonString)

for businfo in json0bj['itemList'] :
    busnum = businfo['rtNm']
    busstop = businfo['stNm']
    arrmsg1 = businfo['arrmsg1']
    arrmsg2 = businfo['arrmsg2']
    plainNo1 = businfo['plainNo1']
    plainNo2 = businfo['plainNo2']


# 노선조회결과 출력

print(" ")
print('===================================================')
print(' ' + busstop + ' 정류장의 ' + busnum + '번 버스의 저상버스 정보입니다.')
print(' ' + arrmsg1, plainNo1)
print(' ' + arrmsg2, plainNo2)
print('===================================================')
print(" ")
ques = str(input(">> 예약을 진행하시겠습니까? : "))


# 응답창에 쓰일 함수선언

def anwserques() :
    print('1. ' + plainNo1)
    print('2. ' + plainNo2)
    print(" ")
    selbus = int(input('>> 예약할 버스를 선택하세요 : '))
    print(" ")

    if selbus == 1 and reservation < 7:
        print(busnum +'번 ' +  plainNo1 + ' 버스의 에약이 정상적으로 처리되었습니다.')

    elif selbus == 2 and reservation < 7 :
        print(busnum + '번 ' + plainNo2 + ' 버스의 예약이 정상적으로 처리되었습니다.')

    elif selbus == 1 and reservation >= 7:
        print('이미 예약된 번호입니다. 다른 차량을 예약해주세요.')

    elif selbus == 2 and reservation >= 7:
        print('이미 예약된 번호입니다. 다른 차량을 예약해주세요.')

    else:
        print('예약이 불가한 번호입니다. 예약이 취소되었습니다.')


# 응답창 구성

if ques == '예' :
    anwserques()
elif ques == '네' :
    anwserques()
elif ques == 'sp' :
    anwserques()
elif ques == 'dP' :
    anwserques()
elif ques == '아니오' :
    print('예약진행이 취소되었습니다.')
elif ques == '아니요' :
    print('예약진행이 취소되었습니다.')
elif ques == 'dksldh' :
    print('예약진행이 취소되었습니다.')
elif ques == 'dksldy' :
    print('예약진행이 취소되었습니다.')
else :
    print('[예, 아니오] 혹은 [네, 아니요]로 응답해주세요.')


# 예약 진행 후 예약 정보를 엑셀에 저장