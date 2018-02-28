import pickle
import sys

import requests


results = []

i = int(sys.argv[1])
j = i + 1000000
print(i, j)

for i in range(i, j):
    url = 'http://services.mcdelivery.co.in/ProcessUser.svc/GetUserProfile'
    customer_id = str(i).zfill(7)
    headers = {'Content-Type': 'application/json', 'CustomerID': customer_id}
    resp = requests.get(url, headers=headers)
    print(resp.text)
    data = resp.json()
    try:
        if data['m'] == 'Record not found' and i % 50 != 0:
            continue
    except:
        print(data)
    results.append(data)
    if i % 50 == 0:
        print(data, i)
        file_name = 'mcd/{}.pkl'.format(i)
        with open(file_name, 'wb') as fh:
            pickle.dump(results, fh)
            results = []
