import requests

def net():
    try:
        responce=requests.get("http://google.com",timeout=6)
        return True
    except(requests.ConnectionError,requests.ConnectTimeout):
        return False


  