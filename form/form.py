import requests

payload = {"username": "jacob", "password": "secure123"}
rr = requests.Request("POST", url="https://httpbin.org/post", data=payload)
rp = requests.post("https://httpbin.org/post", data=payload)
prepared = rr.prepare()
print("rp text", rp.text)
print("prepared", prepared.body)
with open("form.txt", "w") as form:
    form.write(rp.text)
    form.write(prepared.body)
