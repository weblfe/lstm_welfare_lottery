import datetime

import requests

import database.csv_util
from client import client

# 数据请求

# 发送请求的url地址

baseUrl = 'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search'
path = '/kjxx/findDrawNotice'
pageNo = 1

params = {
    'name': 'ssq',
    'issueCount': '',
    'issueStart': '',
    'issueEnd': '',
    'dayStart': '2017-10-24',
    'dayEnd': '2021-08-04',
    'pageNo': pageNo,
}

headers = {
    'Referer': 'http://www.cwl.gov.cn/ygkj/wqkjsp/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

titles = ['期号',
          '开奖日期',
          '红球',
          '蓝球',
          '一等奖中奖注数',
          '一等奖中奖金额',
          '二等奖中奖注数',
          '二等奖中奖金额',
          '三等奖中奖注数',
          '三等奖中奖金额',
          '四等奖中奖注数',
          '四等奖中奖金额',
          '五等奖中奖注数',
          '五等奖中奖金额',
          '六等奖中奖注数',
          '六等奖中奖金额',
          '一等奖中奖地区',
          '奖池金额']


# 双色球
class SSQClient(client.Client):
    __query_path = "/kjxx/findDrawNotice"

    def __init__(self, base_url=""):
        super().__init__(baseUrl=base_url)

    def Query(self, day=0, count=100, page=1):
        body = params.copy()
        now = datetime.datetime.now()
        body["page"] = page
        body["issueCount"] = count
        if day > 0:
            body["dayStart"] = datetime.date(year=now.year, month=now.month, day=now.day - day).strftime("%Y-%m-%d")
            body["dayEnd"] = datetime.date(year=now.year, month=now.month, day=now.day).strftime("%Y-%m-%d")
        return self.call(method="GET", url=self.__query_path, body=body, headers=headers)


if __name__ == "__main__":
    api = SSQClient(baseUrl)
    response = api.Query()
    data = response.json()
    print(data)
    rows = database.csv_util.transform(data["result"])
    database.csv_util.save_dicts(titles, rows)
