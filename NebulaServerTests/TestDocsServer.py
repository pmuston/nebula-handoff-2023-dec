import requests

base_url = "http://localhost:8008"

def test_modules():
    modules = get_url(f"{base_url}/api/modules")
    if modules and len(modules)>0:
        tags = [x['tag'] for x in modules]
        print(tags)
        module = get_url(f"{base_url}/api/modules/{tags[0]}")
        if module:
            for item in module.items():
                print(item)

def get_url(url):
    resp = requests.get(url)
    ok = resp.status_code==200
    if ok:
        return resp.json()
    else:
        print(f"Error getting: {url}")
        return None

def test_fbs():
    fbds = get_url(f"{base_url}/api/fbds")
    if fbds and len(fbds)>0:
        names = [x['name'] for x in fbds]
        print(names)
        fbd = get_url(f"{base_url}/api/fbds/{names[0]}")
        if fbd:
            for item in fbd.items():
                print(item)


test_modules()
print()
test_fbs()