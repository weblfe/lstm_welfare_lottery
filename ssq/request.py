import datetime
import time

import requests
from client import client

# 数据请求

# 发送请求的url地址

baseUrl = 'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search'
path = '/kjxx/findDrawNotice'
page = 1

params = {
    'name': 'ssq',
    'issueCount': '',
    'issueStart': '',
    'issueEnd': '',
    'dayStart': '2017-10-24',
    'dayEnd': '2021-08-04',
    'pageNo': page,
}

headers = {
    'Referer': 'http://www.cwl.gov.cn/ygkj/wqkjsp/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

response = requests.get(url=baseUrl, params=params, headers=headers)


# 双色球
class SSQClient(client.Client):

    __query_path = "/kjxx/findDrawNotice"

    def __init__(self, base_url=""):
        super().__init__(baseUrl=base_url)

    def Query(self):
        body = params.copy()
        now = datetime.datetime.now()
        body["dayStart"] = datetime.date(year=now.year, month=now.month, day=now.day-5).strftime("%Y-%m-%d")
        body["dayEnd"] = datetime.date(year=now.year, month=now.month, day=now.day).strftime("%Y-%m-%d")
        return self.call(method="GET", url=self.__query_path, body=body)


if __name__ == "__main__":
    cli = SSQClient(baseUrl)
    response = cli.Query()
    data = response.json()
    print(data)
