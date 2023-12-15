import requests

base_url = "http://localhost:8004"

def test_modules():
    modules = get_url(f"{base_url}/api/modules")
    if modules and len(modules)>0:
        module = get_url(f"{base_url}/api/modules/{modules[0]}")
        if module:
            for item in module[:10]:
                print(item)

def get_url(url):
    resp = requests.get(url)
    ok = resp.status_code==200
    if ok:
        return resp.json()
    else:
        print(f"Error getting: {url}")
        return None

def test_values():
    modules = get_url(f"{base_url}/api/modules")
    if modules and len(modules)>0:
        module = get_url(f"{base_url}/api/modules/{modules[0]}")
        values = get_url(f"{base_url}/api/modules/{modules[0]}/values")
        paths = {x['path'] for x in module[:5]}
        values = {x['path']:x for x in values}
        for path in paths:
            print(values[path])


test_modules()
print()
test_values()