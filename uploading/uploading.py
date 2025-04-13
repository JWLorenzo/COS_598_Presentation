import requests

files = {"file": open("hello.txt", "rb")}
r = requests.post("https://httpbin.org/post", files=files)
print("r text", r.text)
with open("upload.txt", "w") as upload:
    upload.write(r.text)
