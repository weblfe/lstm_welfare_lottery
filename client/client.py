import requests


class Client:
    basePath = 'http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search'

    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    PATCH = "PATCH"
    HEAD = "HEAD"
    DELETE = "DELETE"
    OPTION = "OPTION"
    TRACE = "TRACE"

    def __init__(self, baseUrl=basePath):
        self.baseUrl = baseUrl

    def call(self, method=POST, url="", body=None, headers=None):
        if headers is None:
            headers = {}
        if body is None:
            body = {}
        method = method.upper()
        if method == self.GET:
            return requests.request(method=method, url=self.makeUrl(url), params=body, headers=headers)
        if method == self.PUT or method == self.POST or method == self.PATCH or method == self.DELETE:
            return requests.request(method=method, url=self.makeUrl(url), data=body, headers=headers)
        else:
            return requests.request(method=method, url=self.makeUrl(url), headers=headers)

    def makeUrl(self, path=""):
        if path == "":
            return self.baseUrl
        if path.find("http://") >= 0 or path.find("https://") >= 0:
            return path
        return self.baseUrl + path
