import requests
response = requests.post("https://httpbin.org/post", data={"Test form": "my_form"})
print(response.text)
#this is not my homework its lessom9.py