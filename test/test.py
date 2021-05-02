import requests

BASE = "http://127.0.0.1:5000/"

# putResponse = requests.put(BASE + "classify/", {'beacon1': 1, 'beacon2': 2, 'beacon3':3, 'location': 0})
# putResponse = requests.put(BASE + "classify/", {'beacon1': 2, 'beacon2': 2, 'beacon3':3, 'location': 0})
# putResponse = requests.put(BASE + "classify/", {'beacon1': 1, 'beacon2': 2, 'beacon3':3, 'location': 0})
# putResponse = requests.put(BASE + "classify/", {'beacon1': 3, 'beacon2': 2, 'beacon3':3, 'location': 0})
# putResponse = requests.put(BASE + "classify/", {'beacon1': 99, 'beacon2': 99, 'beacon3':99, 'location': 1})
getResponse = requests.get(BASE + "classify/", {'beacon1': 8, 'beacon2': 8, 'beacon3': 8})
# response = requests.patch(BASE + "/video/2", {"views": 99, "likes": 9999})
print(getResponse.json())