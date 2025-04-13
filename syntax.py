import requests

r = requests.post(url="https://httpbin.org/post", data={"key": "value"})
print("r text", r.text)
