import requests

s = requests.Session()

s.get("https://httpbin.org/cookies/set/sessioncookie/123456789")
r = s.get("https://httpbin.org/cookies")

print("With session", r.text)

r2 = requests.get("https://httpbin.org/cookies/set/sessioncookie/123456789")
print("Without session:", r2.text)

r3 = requests.get("https://httpbin.org/cookies")
print("Finally:", r3.text)

with open("session.txt", "w") as session:
    session.write(f"{r.text}\n")
    session.write(f"{r2.text}\n")
    session.write(f"{r3.text}\n")
