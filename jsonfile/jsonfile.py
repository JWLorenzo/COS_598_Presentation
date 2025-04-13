import requests

payload = {"username": "jacob", "password": "secure123"}
r = requests.post("https://httpbin.org/post", json=payload)
print("r text", r.text)
with open("jsonfile.txt", "w") as jsonfile:
    jsonfile.write(r.text)
