import requests

class TestHTTP:
    def test_get(self):
        r = requests.get('https://testerhome.com/hogwarts')
        print(r)
    def test_get_query(self):
        url = "https://httpbin.org/#/HTTP_Methods/get_get"
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.get(url, params=payload)
        self.inspect_response(r)
        requests.request()


    def inspect_response(self, r):
        print(r.headers)