import urllib.request
import datetime

#get_request_url 함수선언
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

#API 받아오기 설정
key = '6vj%2BtrHJwPedYTlk7Lad5rfHa7ZjLgbp7he0eRo9O0DoyEJfn8HV2DIKQqdLPypeXvt5tE7c5Oq4cWW3LQzQ4A%3D%3D'
busRouteld = '102000041'

queryParams = 'serviceKey='+key+'&stId='+busRouteld+'&'
url = 'http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId?'+queryParams

print(url)
#req = urllib.request.urlopen(url)
#print(type(req))

#retData = get_request_url(url)
#print(retData)



## API 읽어오기 설정 끝


# xml 읽어오기
import xmltodict

content = requests.get(url).content
dict = xmltodict.parse(content)
print(dict['ServiceResult']['commsgBody']['arrmsg1'])
