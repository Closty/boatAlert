import requests

url ='https://h5.cmskchp.com/querySailingList'

data={
    'trip':'0',
    'startSite' : 'SK',
    'endSite' : 'HKA',
    'goDate' : '2022-09-13'
}

headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
 
            }

a = requests.post(url, json=data,headers =headers).json()['sailingList']

#print(a)


for num in range(2):
    print(num)
    if int(a[num]['totalRemainVolume']) > 0:
        content = '日期：' + a[num]['createTime'] + '\n时间段:'  + a[num]['startTime'] + '-' + a[num]['endTime'] + '\n座位余额：' + a[num]['totalRemainVolume']
        requests.get('通知链接' + content)
    else:
        print('日期：' + a[num]['createTime'] + '\n时间段:'  + a[num]['startTime'] + '-' + a[num]['endTime'] + '\n' + '无座位')
print('\n')
