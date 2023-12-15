import requests

base_url = "http://localhost:8000"

def test_modules():
    resp = requests.get(f"{base_url}/api/modules")
    ok = resp.status_code==200
    modules = None
    if ok:
        print(resp.json())
        modules = resp.json()

    if ok and len(modules)>0:
        resp = requests.get(f"{base_url}/api/modules/{modules[0]}")
        ok = resp.status_code == 200

    if ok:
        for item in resp.json():
            print(item)

test_modules()