from .common import *

def test_requests():
    url = 'http://www.baidu.com'
    r = requests.get(url)
    print(r.status_code)
