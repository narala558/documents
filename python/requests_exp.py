import pickle

import requests


url = 'http://avilpage.com'

# build query url
payload = {'start': 10, 'end': 20}
response = requests.get(url, params=payload)
print(response.url)

resp = requests.post(url, headers={'Authorization': 'Basic foo'})
data = resp.json()


with open('d.pkl', 'wb') as fh:
    pickle.dump(data, fh)


# save image
import requests
import shutil

r = requests.get(settings.STATICMAP_URL.format(**data), stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
