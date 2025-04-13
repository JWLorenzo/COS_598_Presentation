import requests


def postError(url: str, filename: str):

    try:
        r = requests.post(url)
        print("r text", r.text)
        with open(filename, "w") as error:
            error.write(r.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        with open(filename, "w") as error:
            error.write(str(e))


postError("https://httpbin.org/post", "error_fine.txt")
postError("https://localhost/", "error.txt")
